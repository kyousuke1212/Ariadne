API 参考API Copy pageCopy
# preload
### 注意
基于 React 的框架 通常会内置资源处理方案，因此你可能不必手动调用此 API。请查阅框架文档以获取详细信息。
preload 可以预获取期望使用的资源，比如样式表、字体或外部脚本。
```
preload("https://example.com/font.woff2", {as: "font"});
```
参考
- preload(href, options)
用法
- 渲染时进行预加载
- 在事件处理程序中预加载
## 参考
### preload(href, options)
调用 react-dom 中的 preload 函数以实现预加载资源。
```
import { preload } from 'react-dom';function AppRoot() {  preload("https://example.com/font.woff2", {as: "font"});  // ……}
```
参见下方更多示例。
preload 函数向浏览器提供一个提示，告诉它应该开始下载给定的资源，这将会节省时间。
#### 参数
- href：字符串，要下载的资源的 URL。
options：对象，可以包含以下属性：
- as：必需的字符串，表示资源的类型，可能的值 包括 audio、document、embed、fetch、font、image、object、script、style、track、video 与 worker。
- crossOrigin：字符串，表示要使用的 CORS 策略，可能的值为 anonymous 与 use-credentials。当 as 设置为 "fetch" 时是必需的。
- referrerPolicy：字符串，表示在获取时发送的 referer 请求头，可能的值为 no-referrer-when-downgrade（默认值）、no-referrer、origin、origin-when-cross-origin 与 unsafe-url。
- integrity：字符串，为资源的加密哈希，用于 验证其真实性。
- type：字符串，表示资源的 MIME 类型。
- nonce：字符串，表示使用严格内容安全策略时允许资源的 加密随机数。
- fetchPriority：字符串，为获取资源建议的相对优先级，可能的值为 auto（默认值）、high 与 low。
- imageSrcSet：字符串，仅与 as: "image" 一起使用，用于指定 图像的源集。
- imageSizes：字符串，仅与 as: "image" 一起使用，用于指定 图像的尺寸。
#### 返回值
preload 不返回任何值。
#### 注意
对 preload 的多个等效调用与单个调用具有相同的效果。根据以下规则，对 preload 的调用被视为等效：
- 如果两个调用具有相同的 href，则它们是等效的，除非：
- 如果 as 设置为 image，并且两个调用具有相同的 href、imageSrcSet 和 imageSizes，则它们是等效的。
- 在浏览器中，可以在任何情况下调用 preload：例如渲染组件时、Effect 中以及事件处理程序中等等。
- 在服务器端渲染或渲染服务器组件时，只有在渲染组件时调用 preload 或在源自渲染组件的异步上下文中调用时，preload 才会生效。其他任何调用都将被忽略。
## 用法
### 渲染时进行预加载
如果知道组件或其子组件将使用特定资源，那么在渲染组件时调用 preload。
#### 预加载的例子
1. 预加载外部脚本 2. 预加载样式表 3. 预加载字体 4. 预加载图片
#### 第 1 个示例 共 4 个示例: 预加载外部脚本
```
import { preload } from 'react-dom';function AppRoot() {  preload("https://example.com/script.js", {as: "script"});  return ...;}
```
如果希望浏览器立即开始执行脚本（而不仅仅是下载它），请使用 preinit；如果想加载一个 ESM 模块，请使用 preloadModule。
下一个示例
### 在事件处理程序中预加载
在转换到需要外部资源的页面或状态之前，于事件处理程序中调用 preload。这会比在渲染新页面或状态时调用它更早地启动该过程。
```
import { preload } from 'react-dom';function CallToAction() {  const onClick = () => {    preload("https://example.com/wizardStyles.css", {as: "style"});    startWizard();  }  return (    <button onClick={onClick}>Start Wizard</button>  );}
```