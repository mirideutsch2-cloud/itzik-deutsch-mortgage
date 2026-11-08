const {chromium}=require('playwright');const ts=process.argv.slice(3).map(Number);const out=process.argv[2];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:.5});
p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>console.log('LOG',m.text()));
await p.goto('http://localhost:8765/index.html');await p.evaluate(()=>window.ready);
for(const t of ts){await p.evaluate(t=>renderFrame(t),t);await p.screenshot({path:`${out}/t${t.toFixed(2)}.jpg`,type:'jpeg',quality:85})}
await b.close()})()
