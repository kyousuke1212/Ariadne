API 参考 Copy pageCopy
# 过时的 React API
这些 API 从 react 包中导出，但是已经不再推荐在最新代码中使用。参见下方每个 API 对应的页面以查看替代方案。
## 过时的 API
- Children 允许你处理和转化作为 children 的 JSX。查看替代方案。
- cloneElement 允许你使用一个元素作为初始值创建一个新的 React 元素。查看替代方案。
- Component 允许你定义一个 JavaScript class 作为 React 类式组件。查看替代方案。
- createElement 允许你创建一个 React 元素，但是一般会使用 JSX。
- createRef 允许你创建一个可以包含任何值的 ref 对象。查看替代方案。
- forwardRef 允许你使用 ref 将 DOM 节点暴露给父组件。
- isValidElement 检测参数值是否为 React 元素，通常会与 cloneElement. 一起使用。
- PureComponent 与 Component 类似，但是当 props 相同时会跳过重新渲染。查看替代方案。
## 已移除的 API
这些 API 在 React 19 中被移除。
- createFactory：使用 JSX 来替代。
- 类组件：static contextTypes: 使用 static contextType 来替代。
- 类组件：static childContextTypes: 使用 static contextType 来替代。
- 类组件：static getChildContext: 使用 Context 来替代。
- 类组件：static propTypes: 使用 TypeScript 等类型系统来替代。
- 类组件：this.refs: 使用 createRef 来替代。