API 参考组件 Copy pageCopy
# <option>
浏览器内置的 <option> 组件 允许你渲染 <select> 组件的选项（option）。
```
<select>  <option value="someOption">Some option</option>  <option value="otherOption">Other option</option></select>
```
参考
- <option>
用法
- 显示带有选项的选择框
## 参考
### <option>
浏览器内置的 <option> 组件 允许你渲染 <select> 组件的选项（option）。
```
<select>  <option value="someOption">Some option</option>  <option value="otherOption">Other option</option></select>
```
参见下面更多示例。
#### Props
<option> 支持所有 常见的元素属性。
除此之外，<option> 还支持以下属性：
- disabled：布尔值。如果 disabled 为 true，该选项（option）将会被选中，并将展示为暗淡状态（dimmed）。
- label：字符串。指定选项的含义。如果未指定，则使用选项内部的文本。
- value：如果选择了此选项，则在提交表单时将使用此选项的 value 值作为父级 <select> 的值。详细信息请参阅 在提交表单时读取 <select> 值。
#### 注意
- React 不支持在 <option> 上使用 selected 属性。相反，对于非受控选择框，请将此选项的 value 属性传递给父级 <select defaultValue>；对于受控选择框，请使用 <select value> 来控制选择框的值。
## 用法
### 显示带有选项的选择框
渲染一个包含一系列 <option> 组件的 <select>，来展示一个选择框，并给每个 <option> 都设置一个 value 属性，表示要与表单一起提交的数据。
在这里了解更多关于 如何展示一个包含一系列 <option> 组件的 <select> 的信息。
```
App.jsApp.jsReloadClearForkexport default function FruitPicker() {
  return (
    <label>
      选择一个水果：
      <select name="精选水果">
        <option value="苹果">苹果</option>
        <option value="香蕉">香蕉</option>
        <option value="橘子">橘子</option>
      </select>
    </label>
  );
}
```