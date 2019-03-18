const fs = require('fs')
const puppeteer = require('puppeteer');

(async () => {
  try {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('https://bvopen.abrickis.me/#/standings');
    await page.waitForSelector('.category', { timeout: 1000 });

    const body = await page.evaluate(() => {
      return document.querySelector('body').innerHTML;
    });
    // console.log(body);
    
    // const html = await page.evaluate(() => {
    //   return document.body.innerHTML
    // })
    // console.log(html)

    const html = await page.content();
    fs.writeFileSync('result.html', html)

    await browser.close();
  } catch (error) {
    console.log(error);
  }
})();