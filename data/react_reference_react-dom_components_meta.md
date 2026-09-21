API 参考组件 Copy pageCopy
# <meta>
浏览器内置的 <meta> 组件 允许向文档添加元数据。
```
<meta name="keywords" content="React, JavaScript, semantic markup, html" />
```
参考
- <meta>
用法
- 使用元数据向文档添加注释
- 使用元数据为文档中的特定项添加注释
## 参考
### <meta>
渲染 浏览器内置的 <meta> 组件 以向文档添加元数据。可以在任何组件渲染 <meta>，React 将始终将相应的 DOM 元素放置在文档头部。
```
<meta name="keywords" content="React, JavaScript, semantic markup, html" />
```
参见下方更多示例。
#### 属性
<meta> 支持所有 常见元素属性。
它应该有恰好一个以下属性之一：name、httpEquiv、charset 或 itemProp。根据指定的属性，<meta> 组件会执行不同的操作。
- name：字符串，指定要附加到文档的 元数据的类型。
- charset：字符串，指定文档使用的字符集，唯一有效的值是 "utf-8"。
- httpEquiv：字符串，指定用于处理文档的指令。
- itemProp：字符串，指定文档内特定项目的元数据，而不是整个文档。
- content：字符串，当与 name 或 itemProp 属性一起使用时，指定要附加的元数据；或者当与 httpEquiv 属性一起使用时，指定指令的行为。
#### 特殊的渲染行为
无论 <meta> 组件在 React 树中的哪个位置被渲染，React 都会始终将其对应的 DOM 元素放在文档的 <head> 中。<head> 是 <meta> 存在于 DOM 中的唯一有效位置，但如果表示特定页面的组件可以自行渲染 <meta> 组件，则这种做法既方便又保持了可组合性。
但是，有一个例外情况：如果 <meta> 具有 itemProp 属性，则没有特殊行为，因为在这种情况下，它不表示文档的元数据，而是表示页面的特定部分的元数据。
## 用法
### 使用元数据向文档添加注释
可以使用元数据为文档添加关键字、摘要或作者姓名等注释。无论在 React 树中的哪个位置被渲染，React 都会将这些元数据放置在文档的 <head> 中。
```
<meta name="author" content="John Smith" /><meta name="keywords" content="React, JavaScript, semantic markup, html" /><meta name="description" content="API reference for the <meta> component in React DOM" />
```
可以在任何组件中渲染 <meta> 组件。React 将在文档的 <head> 中放置一个 <meta> DOM 节点。
```
App.jsShowRenderedHTML.jsApp.jsReloadClearForkimport ShowRenderedHTML from './ShowRenderedHTML.js';

export default function SiteMapPage() {
  return (
    <ShowRenderedHTML>
      <meta name="keywords" content="React" />
      <meta name="description" content="A site map for the React website" />
      <h1>Site Map</h1>
      <p>...</p>
    </ShowRenderedHTML>
  );
}
```
### 使用元数据为文档中的特定项添加注释
可以使用带有 itemProp 属性的 <meta> 组件来为文档中的特定项添加元数据注释。在这种情况下，React 不会 将这些注释放置在文档 <head> 中，而是像任何其他 React 组件一样放置它们。
```
<section itemScope>  <h3>为特定项添加注释</h3>  <meta itemProp="description" content="API reference for using <meta> with itemProp" />  <p>...</p></section>
```