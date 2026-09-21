API 参考 Copy pageCopy
# 内置的 React API
除了 Hooks 和 Components 之外，react 包还导出了一些其他的 API，这些 API 对于创建组件非常有用。本页面将介绍这些剩余的 React API。
- createContext API 可以创建一个 context，你可以将其提供给子组件，通常会与 useContext 一起配合使用。
- lazy 允许你延迟加载组件，直到该组件需要第一次被渲染。
- memo 允许你在 props 没有变化的情况下跳过组件的重渲染。通常 useMemo 与 useCallback 会一起配合使用。
- startTransition 允许你可以标记一个状态更新是不紧急的。类似于 useTransition。
- act 允许你在测试中包装渲染和交互，以确保在断言之前已完成更新。
## 资源 API
组件可以在不将 资源 作为其 state 一部分的情况下访问。 例如，组件可以从 Promise 中读取消息，或从 context 中读取样式信息。
要从资源中读取一个值，使用以下 API：
- use 让你读取资源的值，比如：Promise 或 context.
```
function MessageComponent({ messagePromise }) {  const message = use(messagePromise);  const theme = use(ThemeContext);  // ...}
```