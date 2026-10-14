// Verificación del HTML final con el transporte de navegador de Archify.
// Uso: node verify.mjs /ruta/a/archify /ruta/al/ejecutable-de-chromium
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const {ChromeVisualBrowser}=await import(pathToFileURL(path.join(process.argv[2],'bin/visual-check.mjs')));
const browser=new ChromeVisualBrowser(process.argv[3]);
const checks=[],viewports=[];
let session;
const assert=(name,ok,evidence)=>{checks.push({name,ok:Boolean(ok),evidence});if(!ok)throw Error(name+': '+JSON.stringify(evidence))};
async function evaluate(expression){const r=await browser.cdp.send('Runtime.evaluate',{expression,returnByValue:true,awaitPromise:true},session);if(r.exceptionDetails)throw Error(JSON.stringify(r.exceptionDetails));return r.result.value;}
async function screenshot(name,full=false){const size=await evaluate('({width:innerWidth,height:document.documentElement.scrollHeight})');const opts={format:'png',fromSurface:true,captureBeyondViewport:full};if(full)opts.clip={x:0,y:0,...size,scale:1};const r=await browser.cdp.send('Page.captureScreenshot',opts,session);fs.writeFileSync(path.join(root,'artifacts',name+'.png'),Buffer.from(r.data,'base64'));}
try{
  session=await browser.sessionPromise;
  const loaded=browser.cdp.waitFor('Page.loadEventFired',session);
  await browser.cdp.send('Page.navigate',{url:pathToFileURL(path.join(root,'index.html')).href},session);await loaded;
  await evaluate('document.fonts.ready');
  for(const [width,height] of [[1440,900],[1600,1000],[1920,1080],[2048,1320],[768,1024],[390,844]]){
    await browser.cdp.send('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:false},session);
    const metrics=await evaluate(`(()=>{const bad=[];document.querySelectorAll('.screen .wireframe text').forEach(t=>{const b=t.getBBox();if(b.x<10||b.x+b.width>170||b.y<10||b.y+b.height>290)bad.push({screen:t.closest('.screen').dataset.id,text:t.textContent,bounds:{x:b.x,y:b.y,width:b.width,height:b.height}})});const sc=document.querySelector('.diagram-scroll');return {width:innerWidth,height:innerHeight,pageWidth:document.documentElement.scrollWidth,pageHeight:document.documentElement.scrollHeight,diagramClient:sc.clientWidth,diagramScroll:sc.scrollWidth,textOverflow:bad}})()`);
    viewports.push(metrics);
    assert('Contención horizontal '+width,metrics.pageWidth<=width,metrics);
    assert('Textos dentro de marcos '+width,metrics.textOverflow.length===0,metrics.textOverflow);
    if(width<1360)assert('Desplazamiento interno móvil '+width,metrics.diagramScroll>metrics.diagramClient,metrics);
    if(width===1440){await evaluate("applyTheme(false)");await screenshot('sketches.light',true);await evaluate("applyTheme(true)");await screenshot('sketches.dark',true);await evaluate("applyTheme(false)");}
    if(width===2048){await evaluate("applyTheme(false)");await screenshot('sketches.large.light',true);await evaluate("applyTheme(true)");await screenshot('sketches.large.dark',true);await evaluate("applyTheme(false)");}
    if(width===390)await screenshot('sketches.mobile',true);
  }
  await browser.cdp.send('Emulation.setDeviceMetricsOverride',{width:1440,height:900,deviceScaleFactor:1,mobile:false},session);
  const count=await evaluate('document.querySelectorAll(".screen").length');assert('14 bocetos originales',count===14,count);
  for(const id of await evaluate('data.screens.map(s=>s.id)')){
    const value=await evaluate(`(()=>{document.querySelector('[data-id="${id}"]').click();return {open:detail.open,title:$('detail-title').textContent,elements:$('detail-elements').children.length,pressed:document.querySelector('[data-id="${id}"]').getAttribute('aria-pressed'),source:$('detail-source').href}})()`);
    assert('Panel '+id,value.open&&value.elements>0&&value.pressed==='true'&&value.title.length>0,value);
    await evaluate('detail.close()');
  }
  await evaluate("setRole('persona')");assert('Selección de rol',await evaluate("document.querySelector('[data-role=negocio]').classList.contains('dimmed') && document.querySelector('[data-role-select=persona]').getAttribute('aria-pressed')==='true'"));
  await evaluate("$('reset').click()");assert('Restablecer',await evaluate("!document.querySelector('.dimmed')&&document.querySelector('[data-role-select=all]').getAttribute('aria-pressed')==='true'"));
  await evaluate("document.querySelector('[data-id=p-chat]').click();$('next').click()");assert('Acción siguiente',await evaluate("selected.id==='p-perfil'&&$('detail-title').textContent==='Perfil del negocio'"));await screenshot('sketches.detail');await evaluate('detail.close()');
  await evaluate("new Promise(resolve=>requestAnimationFrame(()=>{document.querySelector('[data-id=p-acceso]').focus();resolve()}))");
  await browser.cdp.send('Input.dispatchKeyEvent',{type:'keyDown',key:'Enter',code:'Enter',windowsVirtualKeyCode:13,text:'\r',unmodifiedText:'\r'},session);
  await browser.cdp.send('Input.dispatchKeyEvent',{type:'keyUp',key:'Enter',code:'Enter',windowsVirtualKeyCode:13},session);
  assert('Abrir con Enter',await evaluate('detail.open'),await evaluate('({focused:document.activeElement.outerHTML.slice(0,250),selected:selected?.id,open:detail.open})'));
  await browser.cdp.send('Input.dispatchKeyEvent',{type:'keyDown',key:'Escape',code:'Escape',windowsVirtualKeyCode:27},session);
  await browser.cdp.send('Input.dispatchKeyEvent',{type:'keyUp',key:'Escape',code:'Escape',windowsVirtualKeyCode:27},session);
  await evaluate('new Promise(resolve=>requestAnimationFrame(resolve))');
  assert('Escape y devolución del foco',await evaluate("!detail.open&&document.activeElement.dataset.id==='p-acceso'"));
  await evaluate("$('theme').click()");assert('Tema oscuro',await evaluate("document.documentElement.dataset.theme==='dark'&&$('theme').getAttribute('aria-pressed')==='true'"));await evaluate("$('theme').click()");
  await browser.cdp.send('Emulation.setEmulatedMedia',{features:[{name:'prefers-reduced-motion',value:'reduce'}]},session);
  assert('Movimiento reducido',await evaluate("matchMedia('(prefers-reduced-motion:reduce)').matches&&getComputedStyle(document.querySelector('.lane')).transitionDuration==='0s'"));
  await evaluate("$('open-map').click()");
  assert('Mapa Archify integrado',await evaluate("$('map-dialog').open&&$('map-frame').srcdoc.includes('WhatsApp')"));await evaluate("$('map-dialog').close()");
  const bytes=fs.readFileSync(path.join(root,'index.html'));
  const receipt={status:'pass',artifact:{path:'../index.html',sha256:createHash('sha256').update(bytes).digest('hex'),bytes:bytes.length},viewports,checks,visualReview:'pending',note:'El HTML de bocetos permite desplazamiento vertical y desplazamiento horizontal interno en móvil según el alcance solicitado.'};
  fs.writeFileSync(path.join(root,'artifacts/sketches.check.json'),JSON.stringify(receipt,null,2)+'\n');
  console.log(JSON.stringify({status:receipt.status,checks:checks.length,viewports:viewports.length,artifact:receipt.artifact}));
}catch(error){console.error(error);process.exitCode=1;}finally{await browser.close();}
