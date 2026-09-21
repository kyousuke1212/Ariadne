# 服务端渲染 API 
## renderToString() 
* 导出自 vue/server-renderer
* 类型
ts
function renderToString(
input: App | VNode,
context?: SSRContext
): Promise

* 示例
js
import { createSSRApp } from 'vue'
import { renderToString } from 'vue/server-renderer'
const app = createSSRApp({
data: () => ({ msg: 'hello' }),
template: {{ msg }}
})
;(async () => {
const html = await renderToString(app)
console.log(html)
})()

### SSR 上下文 
你可以传入一个可选的上下文对象用来在渲染过程中记录额外的数据，例如访问 Teleport 的内容：
js
const ctx = {}
const html = await renderToString(app, ctx)
console.log(ctx.teleports) // { '#teleported': 'teleported content' }

这个页面中的其他大多数 SSR API 也可以接受一个上下文对象。该上下文对象可以在组件代码里通过 useSSRContext 辅助函数进行访问。
* 参考指南 - 服务端渲染 (SSR)
## renderToNodeStream() 
将输入渲染为一个 Node.js Readable stream 实例。
* 导出自 vue/server-renderer
* 类型
ts
function renderToNodeStream(
input: App | VNode,
context?: SSRContext
): Readable

* 示例
js
// 在一个 Node.js http 处理函数内
renderToNodeStream(app).pipe(res)

vue/server-renderer 的 ESM 构建不支持此方法，因为它是与 Node.js 环境分离的。请换为使用 pipeToNodeWritable。
## pipeToNodeWritable() 
将输入渲染并 pipe 到一个 Node.js Writable stream 实例。
* 导出自 vue/server-renderer
* 类型
ts
function pipeToNodeWritable(
input: App | VNode,
context: SSRContext = {},
writable: Writable
): void

* 示例
js
// 在一个 Node.js http 处理函数内
pipeToNodeWritable(app, {}, res)

## renderToWebStream() 
将输入渲染为一个 Web ReadableStream 实例。
* 导出自 vue/server-renderer
* 类型
ts
function renderToWebStream(
input: App | VNode,
context?: SSRContext
): ReadableStream

* 示例
js
// 在一个支持 ReadableStream 的环境下
return new Response(renderToWebStream(app))

在不能全局暴露 ReadableStream 构造函数的环境下，请换为使用 pipeToWebWritable()。
## pipeToWebWritable() 
将输入渲染并 pipe 到一个 Web WritableStream 实例。
* 导出自 vue/server-renderer
* 类型
ts
function pipeToWebWritable(
input: App | VNode,
context: SSRContext = {},
writable: WritableStream
): void

* 示例
通常与 TransformStream 结合使用：
js
// 诸如 CloudFlare worker 这样的环境中，TransformStream 是可用的。
// 在 Node.js 中，TransformStream 需要从 'stream/web' 显式导入。
const { readable, writable } = new TransformStream()
pipeToWebWritable(app, {}, writable)
return new Response(readable)

## renderToSimpleStream() 
通过一个简单的接口，将输入以 stream 模式进行渲染。
* 导出自 vue/server-renderer
* 类型
ts
function renderToSimpleStream(
input: App | VNode,
context: SSRContext,
options: SimpleReadable
): SimpleReadable
interface SimpleReadable {
push(content: string | null): void
destroy(err: any): void
}

* 示例
js
let res = ''
renderToSimpleStream(
app,
{},
{
push(chunk) {
if (chunk === null) {
// done
console(render complete: ${res})
} else {
res += chunk
}
},
destroy(err) {
// error encountered
}
}
)

## useSSRContext() 
一个运行时 API，用于获取已传递给 renderToString() 或其他服务端渲染 API 的上下文对象。
* 类型
ts
function useSSRContext>(): T | undefined

* 示例
得到的上下文能够作为附加信息用于渲染最终的 HTML (例如 head 中的元数据)。
vue

import { useSSRContext } from 'vue'
// 确保只在服务端渲染时调用
// https://cn.vite.dev/guide/ssr.html#conditional-logic
if (import.meta.env.SSR) {
const ctx = useSSRContext()
// ...给上下文对象添加属性
}


## data-allow-mismatch  
可以消除激活不匹配警告的特殊 attribute。
* 示例
html
{{ data.toLocaleString() }}

值可以限制不匹配为特定类型。允许的值有：
* text
* children (仅允许直接子组件不匹配)
* class
* style
* attribute
如果没有提供值，则会允许所有类型的不匹配。