API 参考组件 Copy pageCopy
# <progress>
浏览器内置的 <progress> 组件 允许你渲染一个进度指示器。
```
<progress value={0.5} />
```
参考
- <progress>
用法
- 控制进度指示器
## 参考
### <progress>
使用 浏览器内置的 <progress> 组件 渲染一个进度指示器。
```
<progress value={0.5} />
```
参见下面更多示例。
#### 参数
<progress> 支持所有 常见的元素属性。
除此之外，<progress> 还支持以下属性：
- max：一个数字，表示指定的最大 value。默认值为 1。
- value：一个介于 0 至 max 之间的数字。如果不确定具体的进度，那么该值可以为 null。value 表示完成了多少进度。
## 用法
### 控制进度指示器
使用 <progress> 组件渲染进度指示器。你可以传递一个介于 0 和指定的 max 值之间的数字 value。如果不传递 max 参数，那么 max 默认值为 1。
如果相关操作未持续进行，请传递 value={null} 将进度指示器设置为不确定状态。
```
App.jsApp.jsReloadClearForkexport default function App() {
  return (
    <>
      <progress value={0} />
      <progress value={0.5} />
      <progress value={0.7} />
      <progress value={75} max={100} />
      <progress value={1} />
      <progress value={null} />
    </>
  );
}
```