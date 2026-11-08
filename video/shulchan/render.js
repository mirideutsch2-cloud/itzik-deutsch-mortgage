const {chromium}=require('playwright');
const [,,out,fps,dur,scale,wi,wn]=process.argv;const F=Math.round(+fps*+dur);
(async()=>{const b=await chromium.launch({args:['--use-gl=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:+scale});
await p.goto('http://localhost:8765/index.html');await p.evaluate(()=>window.ready);
for(let f=+wi;f<F;f+=+wn){await p.evaluate(t=>renderFrame(t),f/+fps);await p.screenshot({path:`${out}/f${String(f).padStart(5,'0')}.jpg`,type:'jpeg',quality:92})}
await b.close()})()
