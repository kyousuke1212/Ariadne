API 参考 Copy pageCopy
# React DOM API
react-dom 包包含一些仅支持在浏览器 DOM 环境下运行的方法，不支持在 React Native 中使用。
## API
这些 API 可以在你的组件中导入，但是很少使用：
- createPortal 允许你将子组件渲染到 DOM 树的不同位置。
- flushSync 允许你强制 React 同步刷新状态并更新 DOM。
## 资源预加载 API
一旦你确定会用到某些资源，这些 API 可用于预加载脚本、样式表和字体等资源，从而让应用更快。例如，在跳转到将使用这些资源的另一个页面之前加载。
基于 React 的框架 通常会为你处理资源加载，因此你可能无需手动调用这些 API。具体请查阅你的框架文档。
- prefetchDNS 让你预取出希望连接的 DNS 域名的 IP 地址。
- preconnect 让你连接到预计请求资源的服务器，即使你尚不确定具体需要哪些资源。
- preload 让你获取预计要使用的样式表、字体、图片或外部脚本。
- preloadModule 让你获取预计要使用的 ESM 模块。
- preinit 让你获取并执行外部脚本，或获取并插入样式表。
- preinitModule 让你获取并执行一个 ESM 模块。
## 入口
react-dom 包提供了两个额外的入口：
- react-dom/client 包含在客户端（在浏览器中）渲染 React 组件的 API。
- react-dom/server 包含在服务器上渲染 React 组件的 API。
## 已移除的 API
这些 API 将在 React 19 中被移除。
- findDOMNode：查看 替代方案。
- hydrate：使用 hydrateRoot 来替代。
- render：使用 createRoot 来替代。
- unmountComponentAtNode：使用 root.unmount() 来替代。
- renderToNodeStream：使用 react-dom/server API 来替代。
- renderToStaticNodeStream：使用 react-dom/server API 来替代。