API 参考API Copy pageCopy
# preinit
### 注意
基于 React 的框架 通常会内置资源处理方案，因此你可能不必手动调用此 API。请查阅框架文档以获取详细信息。
preinit 可以预获取和评估样式表或外部脚本。
```
preinit("https://example.com/script.js", {as: "script"});
```
参考
- preinit(href, options)
用法
- 渲染时预初始化
- 在事件处理程序中预初始化
## 参考
### preinit(href, options)
调用 react-dom 中的 preinit 函数以实现预初始化脚本或样式表。
```
import { preinit } from 'react-dom';function AppRoot() {  preinit("https://example.com/script.js", {as: "script"});  // ……}
```
参见下方更多示例。
preinit 函数向浏览器提供一个提示，告诉它应该开始下载并执行给定的资源，这可以节省时间。preinit 的脚本在下载完成后执行。预初始化的样式表被插入到文档中，这会使它们立即生效。
#### 参数
- href：字符串，要下载并执行的资源的 URL。
options：对象，可以包含以下属性：
- as：必需的字符串，表示资源的类型，可能的值包括 script 与 style。
- precedence：字符串，与样式表一起使用时必需。指定样式表相对于其他样式表的插入位置。具有较高优先级的样式表可以覆盖具有较低优先级的样式表，可能的值包括 reset、low、medium 与 high。
- crossOrigin：字符串，表示要使用的 CORS 策略，可能的值为 anonymous 与 use-credentials。
- integrity：字符串，为资源的加密哈希，用于 验证其真实性。
- nonce：字符串，表示使用严格内容安全策略时允许资源的 加密随机数。
- fetchPriority：字符串，表示建议获取资源的相对优先级，可能的值为 auto（默认值）、high 与 low。
#### 返回值
preinit 不返回任何值。
#### 注意
- 对于具有相同 href 的多个 preinit 调用具有与单个调用相同的效果。
- 在浏览器中，可以在任何情况下调用 preinit：例如渲染组件时、Effect 中以及事件处理程序中等等。
- 在服务器端渲染或渲染服务器组件时，只有在渲染组件时调用 preinit 或在源自渲染组件的异步上下文中调用时，preinit 才会生效。其他任何调用都将被忽略。
## 用法
### 渲染时预初始化
如果知道组件或其子组件将使用特定资源，并且可以接受资源被评估并在下载后立即生效，请在渲染组件时调用 preinit。
#### 预初始化的例子
1. 预初始化外部脚本 2. 预初始化样式表
#### 第 1 个示例 共 2 个示例: 预初始化外部脚本
```
import { preinit } from 'react-dom';function AppRoot() {  preinit("https://example.com/script.js", {as: "script"});  return ...;}
```
如果希望浏览器下载脚本但不立即执行它，请使用 preload。如果想加载一个 ESM 模块，请使用 preinitModule。
下一个示例
### 在事件处理程序中预初始化
在转换到需要外部资源的页面或状态之前，于事件处理程序中调用 preinit。这会比在渲染新页面或状态时调用它更早地启动该过程。
```
import { preinit } from 'react-dom';function CallToAction() {  const onClick = () => {    preinit("https://example.com/wizardStyles.css", {as: "style"});    startWizard();  }  return (    <button onClick={onClick}>Start Wizard</button>  );}
```