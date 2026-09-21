API 参考 Copy pageCopy
# React DOM 组件
React 支持所有浏览器内置的 HTML 与 SVG 组件。
## 通用组件
所有的浏览器内置组件都支持一些共同的属性与方法。
- 通用组件（如 <div>）
这些组件在 React 中可以使用 React 特有的属性，如 ref 与 dangerouslySetInnerHTML。
## 表单组件
这些浏览器内置组件接收用户的输入：
- <input>
- <select>
- <textarea>
将 value 作为 prop 传递给这些组件会将其变为 受控组件。
## 资源和元数据组件
通过这些内置浏览器组件，您可以加载外部资源或为文档添加元数据注释：
- <link>
- <meta>
- <script>
- <style>
- <title>
它们在 React 中是特殊的，因为 React 可以将它们渲染到文档头部，在资源加载时暂停，并执行参考页面中针对每个特定组件描述的其他行为。
## 所有的 HTML 组件
React 支持所有浏览器内置的组件，包括：
- <aside>
- <audio>
- <b>
- <base>
- <bdi>
- <bdo>
- <blockquote>
- <body>
- <br>
- <button>
- <canvas>
- <caption>
- <cite>
- <code>
- <col>
- <colgroup>
- <data>
- <datalist>
- <dd>
- <del>
- <details>
- <dfn>
- <dialog>
- <div>
- <dl>
- <dt>
- <em>
- <embed>
- <fieldset>
- <figcaption>
- <figure>
- <footer>
- <form>
- <h1>
- <head>
- <header>
- <hgroup>
- <hr>
- <html>
- <i>
- <iframe>
- <img>
- <input>
- <ins>
- <kbd>
- <label>
- <legend>
- <li>
- <link>
- <main>
- <map>
- <mark>
- <menu>
- <meta>
- <meter>
- <nav>
- <noscript>
- <object>
- <ol>
- <optgroup>
- <option>
- <output>
- <p>
- <picture>
- <pre>
- <progress>
- <q>
- <rp>
- <rt>
- <ruby>
- <s>
- <samp>
- <script>
- <section>
- <select>
- <slot>
- <small>
- <source>
- <span>
- <strong>
- <style>
- <sub>
- <summary>
- <sup>
- <table>
- <tbody>
- <td>
- <template>
- <textarea>
- <tfoot>
- <th>
- <thead>
- <time>
- <title>
- <tr>
- <track>
- <u>
- <ul>
- <var>
- <video>
- <wbr>
### 注意
与 DOM 标准 类似，React 使用 camelCase 命名约定来命名 props。例如，你应该使用 tabIndex 而不是 tabindex。你可以使用 在线转换器 将现有的 HTML 转换为 JSX。
### 自定义 HTML 元素
如果你渲染一个带有连字符的标签，如 <my-element>，React 会认为你想要渲染一个 自定义 HTML 元素。
如果你使用 is 属性渲染一个内置的浏览器 HTML 元素，它也会被视为自定义元素。
#### 在自定义元素上设置值
自定义元素有两种数据传递方法：
- Attributes：显示在标记中，只能设置为字符串值
- Properties：不在标记中显示，可设置为任意 JavaScript 值
默认情况下，React 会将 JSX 中绑定的值作为 attributes 传递：
```
<my-element value="Hello, world!"></my-element>
```
默认情况下，传递给自定义元素的非字符串 JavaScript 值将被序列化：
```
// 将以 `[1,2,3].toString()` 的输出结果 `"1,2,3"` 的形式传递<my-element value={[1,2,3]}></my-element>
```
不过，如果自定义元素的属性名称在构建过程中出现在类上，React 就会将其识别为可以传递任意值的 arbitrary：
```
MyElement.jsApp.jsMyElement.jsReloadClearForkexport class MyElement extends HTMLElement {
  constructor() {
    super();
    // 初始化为元素时
    // 此处的值将被 React 覆盖
    this.value = undefined;
  }

  connectedCallback() {
    this.innerHTML = this.value.join(", ");
  }
}
```
#### 监听自定义元素上的事件
使用自定义元素时的一个常见模式是，它们可能会派发 自定义事件，而不是在事件发生时接受函数调用。在通过 JSX 绑定事件时，可以使用 on 前缀来监听这些事件。
```
MyElement.jsApp.jsApp.jsReloadClearForkexport function App() {
  return (
    <my-element
      onspeak={e => console.log(e.detail.message)}
    ></my-element>
  )
}
```
### 注意
事件区分大小写，并支持破折号（-）。在监听自定义元素事件时，请保留事件的大小写并包含所有破折号：
```
// 监听 `say-hi` 事件<my-element onsay-hi={console.log}></my-element>// 监听 `sayHi` 事件<my-element onsayHi={console.log}></my-element>
```
## 所有 SVG 组件
React 支持所有浏览器内置的 SVG 组件，包括：
- <a>
- <animate>
- <animateMotion>
- <animateTransform>
- <circle>
- <clipPath>
- <defs>
- <desc>
- <discard>
- <ellipse>
- <feBlend>
- <feColorMatrix>
- <feComponentTransfer>
- <feComposite>
- <feConvolveMatrix>
- <feDiffuseLighting>
- <feDisplacementMap>
- <feDistantLight>
- <feDropShadow>
- <feFlood>
- <feFuncA>
- <feFuncB>
- <feFuncG>
- <feFuncR>
- <feGaussianBlur>
- <feImage>
- <feMerge>
- <feMergeNode>
- <feMorphology>
- <feOffset>
- <fePointLight>
- <feSpecularLighting>
- <feSpotLight>
- <feTile>
- <feTurbulence>
- <filter>
- <foreignObject>
- <g>
- <hatch>
- <hatchpath>
- <image>
- <line>
- <linearGradient>
- <marker>
- <mask>
- <metadata>
- <mpath>
- <path>
- <pattern>
- <polygon>
- <polyline>
- <radialGradient>
- <rect>
- <script>
- <set>
- <stop>
- <style>
- <svg>
- <switch>
- <symbol>
- <text>
- <textPath>
- <title>
- <tspan>
- <use>
- <view>
### 注意
与 DOM 标准 类似，React 使用 camelCase 命名约定来命名 props。例如，你应该使用 tabIndex 而不是 tabindex。你可以使用 在线转换器 将现有的 SVG 转换为 JSX。
命名空间属性（attribute）也必须写成没有冒号的形式：
- xlink:actuate 改为 xlinkActuate。
- xlink:arcrole 改为 xlinkArcrole。
- xlink:href 改为 xlinkHref。
- xlink:role 改为 xlinkRole。
- xlink:show 改为 xlinkShow。
- xlink:title 改为 xlinkTitle。
- xlink:type 改为 xlinkType。
- xml:base 改为 xmlBase。
- xml:lang 改为 xmlLang。
- xml:space 改为 xmlSpace。
- xmlns:xlink 改为 xmlnsXlink。