# 快速上手 
## 线上尝试 Vue 
* 想要快速体验 Vue，你可以直接试试我们的演练场。
* 如果你更喜欢不用任何构建的原始 HTML，可以使用 JSFiddle 入门。
* 如果你已经比较熟悉 Node.js 和构建工具等概念，还可以直接在浏览器中打开 StackBlitz 来尝试完整的构建设置。
* 要了解推荐的设置流程，请观看这个互动式 Scrimba 教程，它将向你展示如何运行、编辑和部署你的第一个 Vue 应用程序。
## 创建一个 Vue 应用 
* 熟悉命令行
* 已安装 ^22.18.0 || >=24.12.0 版本的 Node.js
在本节中，我们将介绍如何在本地搭建 Vue 单页应用。创建的项目将使用基于 Vite 的构建设置，并允许我们使用 Vue 的单文件组件 (SFC)。
确保你安装了最新版本的 Node.js，并且你的当前工作目录正是打算创建项目的目录。在命令行中运行以下命令 (不要带上 $ 符号)：
sh [npm]
$ npm create vue@latest

sh [pnpm]
$ pnpm create vue@latest

sh [yarn]
# For Yarn (v1+)
$ yarn create vue
# For Yarn Modern (v2+)
$ yarn create vue@latest
# For Yarn ^v4.11
$ yarn dlx create-vue@latest

sh [bun]
$ bun create vue@latest

这一指令将会安装并执行 create-vue，它是 Vue 官方的项目脚手架工具。你将会看到一些诸如 TypeScript 和测试支持之类的可选功能提示：
如果不确定是否要开启某个功能，你可以直接按下回车键选择 No。在项目被创建后，通过以下步骤安装依赖并启动开发服务器：
sh-vue [npm]
$ cd {{''}}
$ npm install
$ npm run dev

sh-vue [pnpm]
$ cd {{''}}
$ pnpm install
$ pnpm run dev

sh-vue [yarn]
$ cd {{''}}
$ yarn
$ yarn dev

sh-vue [bun]
$ cd {{''}}
$ bun install
$ bun run dev

你现在应该已经运行起来了你的第一个 Vue 项目！请注意，生成的项目中的示例组件使用的是组合式 API 和 ，而非选项式 API。下面是一些补充提示：
* 推荐的 IDE 配置是 Visual Studio Code + Vue - Official 扩展。如果使用其他编辑器，参考 IDE 支持章节。
* 更多工具细节，包括与后端框架的整合，我们会在工具链指南进行讨论。
* 要了解构建工具 Vite 更多背后的细节，请查看 Vite 文档。
* 如果你选择使用 TypeScript，请阅读 TypeScript 使用指南。
当你准备将应用发布到生产环境时，请运行：
sh [npm]
$ npm run build

sh [pnpm]
$ pnpm run build

sh [yarn]
$ yarn build

sh [bun]
$ bun run build

此命令会在 ./dist 文件夹中为你的应用创建一个生产环境的构建版本。关于将应用上线生产环境的更多内容，请阅读生产环境部署指南。
下一步>
## 通过 CDN 使用 Vue 
你可以借助 script 标签直接通过 CDN 来使用 Vue：
html


这里我们使用了 unpkg，但你也可以使用任何提供 npm 包服务的 CDN，例如 jsdelivr 或 cdnjs。当然，你也可以下载此文件并自行提供服务。
通过 CDN 使用 Vue 时，不涉及“构建步骤”。这使得设置更加简单，并且可以用于增强静态的 HTML 或与后端框架集成。但是，你将无法使用单文件组件 (SFC) 语法。
### 使用全局构建版本 
上面的链接使用了*全局构建版本*的 Vue，该版本的所有顶层 API 都以属性的形式暴露在了全局的 Vue 对象上。这里有一个使用全局构建版本的例子：
html

{{ message }}

const { createApp } = Vue
createApp({
data() {
return {
message: 'Hello Vue!'
}
}
}).mount('#app')


CodePen 示例 >
html

{{ message }}

const { createApp, ref } = Vue
createApp({
setup() {
const message = ref('Hello vue!')
return {
message
}
}
}).mount('#app')


CodePen 示例 >
本指南中许多关于组合式 API 的例子将使用  语法，这需要构建工具。如果你打算在没有构建步骤的情况下使用组合式 API，请参考 setup() 选项的用法。
### 使用 ES 模块构建版本 
在本文档的其余部分我们使用的主要是 ES 模块语法。现代浏览器大多都已原生支持 ES 模块。因此我们可以像这样通过 CDN 以及原生 ES 模块使用 Vue：
html{3,4}
{{ message }}

import { createApp } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
createApp({
data() {
return {
message: 'Hello Vue!'
}
}
}).mount('#app')


html{3,4}
{{ message }}

import { createApp, ref } from 'https://unpkg.com/vue@3/dist/vue.esm-browser.js'
createApp({
setup() {
const message = ref('Hello Vue!')
return {
message
}
}
}).mount('#app')


注意我们使用了 ，且导入的 CDN URL 指向的是 Vue 的 ES 模块构建版本。
CodePen 示例 >
CodePen 示例 >
### 启用 Import maps 
在上面的示例中，我们使用了完整的 CDN URL 来导入，但在文档的其余部分中，你将看到如下代码：
js
import { createApp } from 'vue'

我们可以使用导入映射表 (Import Maps) 来告诉浏览器如何定位到导入的 vue：
html{1-7,12}

{
"imports": {
"vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
}
}

{{ message }}

import { createApp } from 'vue'
createApp({
data() {
return {
message: 'Hello Vue!'
}
}
}).mount('#app')


CodePen 示例 >
html{1-7,12}

{
"imports": {
"vue": "https://unpkg.com/vue@3/dist/vue.esm-browser.js"
}
}

{{ message }}

import { createApp, ref } from 'vue'
createApp({
setup() {
const message = ref('Hello Vue!')
return {
message
}
}
}).mount('#app')


CodePen 示例 >
你也可以在映射表中添加其他的依赖——但请务必确保你使用的是该库的 ES 模块版本。
导入映射表是一个相对较新的浏览器功能。请确保使用其支持范围内的浏览器。请注意，只有 Safari 16.4 以上版本支持。
到目前为止示例中使用的都是 Vue 的开发构建版本——如果你打算在生产中通过 CDN 使用 Vue，请务必查看生产环境部署指南。
虽然 Vue 可以不依赖构建系统使用，但也可以考虑使用 vuejs/petite-vue 这个替代方案，以更好地适配可能在 jquery/jquery (过去) 或 alpinejs/alpine (现在) 的上下文中使用的情况。
### 拆分模块 
随着对这份指南的逐步深入，我们可能需要将代码分割成单独的 JavaScript 文件，以便更容易管理。例如：
html [index.html]


import { createApp } from 'vue'
import MyComponent from './my-component.js'
createApp(MyComponent).mount('#app')


js [my-component.js]
export default {
data() {
return { count: 0 }
},
template: Count is: {{ count }}
}

js [my-component.js]
import { ref } from 'vue'
export default {
setup() {
const count = ref(0)
return { count }
},
template: Count is: {{ count }}
}

如果直接在浏览器中打开了上面的 index.html，你会发现它抛出了一个错误，因为 ES 模块不能通过 file:// 协议工作，也即是当你打开一个本地文件时浏览器使用的协议。
由于安全原因，ES 模块只能通过 http:// 协议工作，也即是浏览器在打开网页时使用的协议。为了使 ES 模块在我们的本地机器上工作，我们需要使用本地的 HTTP 服务器，通过 http:// 协议来提供 index.html。
要启动一个本地的 HTTP 服务器，请先安装 Node.js，然后通过命令行在 HTML 文件所在文件夹下运行 npx serve。你也可以使用其他任何可以基于正确的 MIME 类型服务静态文件的 HTTP 服务器。
可能你也注意到了，这里导入的组件模板是内联的 JavaScript 字符串。如果你正在使用 VS Code，你可以安装 es6-string-html 扩展，然后在字符串前加上一个前缀注释 /*html*/ 以高亮语法。
## 框架 
有一些 Vue 框架开箱即用地支持 SSR 及其他功能：
* Nuxt
* Vike
* Astro
* Quasar
通常建议仅在你需要 SSR 时才使用框架。
如果你不需要 SSR，可以直接使用 Vite (这正是上文创建一个 Vue 应用章节所搭建的内容)。
Vue 框架通常在底层使用 Vite，因此如果你不需要 SSR，直接使用 Vite 而非 Vue 框架会是更简单的配置。不过，框架也支持一些额外功能，比如 UI 主题，这也可能是选择 Vue 框架而非单纯使用 Vite 的理由。
## 下一步 
如果你尚未阅读简介，我们强烈推荐你在移步到后续文档之前返回去阅读一下。