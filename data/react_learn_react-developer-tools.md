学习 React配置 Copy pageCopy
# React 开发者工具
使用 React 开发者工具检查 React components，编辑 props 和 state，并识别性能问题。
### 你将会学习到
- 如何安装 React 开发者工具
## 浏览器扩展
调试 React 构建的网站最简单的办法就是安装 React 开发者工具浏览器扩展。它可用于几种流行的浏览器：
- 安装 Chrome 扩展
- 安装 Firefox 扩展
- 安装 Edge 扩展
现在，如果你访问一个用 React 构建 的网站，你将看到 Components 和 Profiler 面板。
### Safari 和其他浏览器
为其他浏览器（比如，Safari），安装 react-devtools npm 包:
```
# Yarnyarn global add react-devtools# Npmnpm install -g react-devtools
```
接下来从终端打开开发者工具：
```
react-devtools
```
然后通过将以下 <script> 标签添加到你网站的 <head> 开头来连接你的网站：
```
<html>  <head>    <script src="http://localhost:8097"></script>
```
现在在浏览器里刷新你的网站，你可以在开发者工具里查看它。
## 移动端（React Native）
你可以使用 React Native DevTools 来检查 React Native 应用程序，它的内置调试器与 React Developer Tools 进行了深度集成。所有功能与浏览器扩展的工作方式相同，包括本机元素突出显示和选择。
了解有关调试 React Native 的更多信息。
对于 React Native 0.76 之前的版本，请按照上面的 Safari and other browsers 指南独立构建 React DevTools。