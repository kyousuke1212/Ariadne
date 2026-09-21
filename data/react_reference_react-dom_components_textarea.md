API 参考组件 Copy pageCopy
# <textarea>
浏览器内置的 <textarea> 组件 允许你渲染一个多行文本输入框。
```
<textarea />
```
参考
- <textarea>
用法
- 展示一个文本框
- 为文本框提供 label 属性
- 提供初始值
- 提交表单时读取文本框的值
- 使用 state 控制文本框
故障排除
- 输入时文本框没有更新
- 当我输入时，文本框光标会跳到开头
- 收到错误：“A component is changing an uncontrolled input to be controlled”
## 参考
### <textarea>
使用 浏览器内置的 <textarea> 组件 渲染一个多行文本输入框。
```
<textarea name="postContent" />
```
参见下面更多示例。
#### 属性
<textarea> 支持所有 常见的元素属性。
你可以通过传递 value 属性 以控制文本框。
- value：一个字符串，用于控制文本框内的文本。
当你传递 value 时，你必须同时传递一个 onChange 处理函数，用于更新传递的值。
如果 <textarea> 是非受控组件，那么你应该传递 defaultValue 参数：
- defaultValue：一个字符串，表示文本框的 初始值。
以下 <textarea> 属性均可用于受控与非受控组件：
- autoComplete：可以为 'on' 或 'off'，表示自动完成的行为。
- autoFocus：布尔值。如果为 true，React 将在挂载时聚焦该元素。
- children：<textarea> 不接受子元素，如果要设置初始值，请使用 defaultValue。
- cols：数字，表示默认宽度，以平均字符宽度计算。默认为 20。
- disabled：布尔值。如果为 true，则输入框将不可交互且显示为禁用状态（dimmed）。
- form：字符串，表示此文本框所属的 <form> 的 id。如果未指定，则为最近的父表单。
- maxLength：数字，表示文本的最大长度。
- minLength：数字，表示文本的最小长度。
- name：字符串，表示在表单提交时与此输入框关联的名称。
- onChange：一个 Event 处理函数。对于 受控文本框，在用户更改输入值时立即触发（例如，对于每个按键）。此行为类似于浏览器 input 事件。
- onChangeCapture：与 onChange 类似，但是是在 捕获阶段 触发。
- onInput：一个 Event 处理函数。在用户更改值时立即触发。由于历史原因，在 React 习惯于使用工作方式类似的 onChange。
- onInputCapture：与 onInput 类似，但是是在 捕获阶段 触发。
- onInvalid：一个 Event 处理函数。如果输入的内容在表单提交时未通过验证，则会触发此事件。与内置的 invalid 事件不同，React 的 onInvalid 事件可以进行冒泡。
- onInvalidCapture：与 onInvalid 类似，但是是在 捕获阶段 触发。
- onSelect：一个 Event 处理函数。当 <textarea> 的选择内容发生变化后触发。React 扩展了 onSelect 事件，还会在空选择和编辑（可能会影响选择）时触发。
- onSelectCapture: 与 onSelect 类似，但是是在 捕获阶段 触发。
- placeholder：字符串，表示当文本框的值为空时，以淡色显示的占位符。
- readOnly：布尔值，如果为 true，文本框将无法被用户编辑。
- required：布尔值，如果为 true，则必须提供值才能在表单中提交。
- rows：数字，表示默认高度，以平均字符高度计算。默认为 2。
- wrap：可以是 'hard'、'soft' 或 'off' 中的一个值，表示提交表单时文本应如何换行。
#### 注意
- 不允许传递像 <textarea>something</textarea> 这样的子元素，你应该 使用 defaultValue 提供初始值。
- 如果一个文本框接收字符串类型的 value 属性，那么它将被视为 受控组件。
- 一个文本框不能同时既是受控组件又是非受控组件。
- 一个文本框在其生命周期内无法在受控和非受控之间切换。
- 每个受控文本框都需要一个 onChange 事件处理程序，以同步更新其后面的新值。
## 用法
### 展示一个文本框
使用 <textarea> 渲染文本框。你可以使用 rows 和 cols 属性指定其默认大小，但默认情况下用户可以调整大小。如果要禁用调整大小功能，可以在 CSS 中指定 resize: none。
```
App.jsApp.jsReloadClearForkexport default function NewPost() {
  return (
    <label>
      写下你的贴子：
      <textarea name="postContent" rows={4} cols={40} />
    </label>
  );
}
```
### 为文本框提供 label 属性
一般而言，应该将每个 <textarea> 都放置在 <label> 内，表示此标签与该选择框相关联。当用户单击标签时，浏览器将自动聚焦选择框。这对于可访问性也非常重要：当用户聚焦选择框时，屏幕阅读器将宣布标签标题。
如果无法将 <textarea> 放置在 <label> 内，请通过将相同的 ID 传递给 <textareaid> 与 <label htmlFor> 来将它们关联起来。为了避免组件在多个实例之间产生冲突，使用 useId 生成这样的 ID。
```
App.jsApp.jsReloadClearForkimport { useId } from 'react';

export default function Form() {
  const postTextAreaId = useId();
  return (
    <>
      <label htmlFor={postTextAreaId}>
        写下你的贴子：
      </label>
      <textarea
        id={postTextAreaId}
        name="postContent"
        rows={4}
        cols={40}
      />
    </>
  );
}
```
显示更多
### 提供初始值
使用 defaultValue 属性传递字符串，指定文本框初始值。
```
App.jsApp.jsReloadClearForkexport default function EditPost() {
  return (
    <label>
      编辑你的贴子：
      <textarea
        name="postContent"
        defaultValue="I really enjoyed biking yesterday!"
        rows={4}
        cols={40}
      />
    </label>
  );
}
```
### 陷阱
与 HTML 不同，像这样传递初始值 <textarea>Some content</textarea> 将不受支持。
### 提交表单时读取文本框的值
在文本框周围添加一个包含 <button type="submit"> 按钮的 <form> 组件。这将调用 <form onSubmit> 事件处理程序。默认情况下，浏览器将向当前 URL 发送表单数据并刷新页面。你可以通过调用 e.preventDefault() 取消此默认行为，并使用 new FormData(e.target) 读取表单数据。
```
App.jsApp.jsReloadClearForkexport default function EditPost() {
  function handleSubmit(e) {
    // 阻止浏览器重新加载页面
    e.preventDefault();

    // 读取表单数据
    const form = e.target;
    const formData = new FormData(form);

    // 你可以直接将 formData 作为 fetch 请求的 body：
    fetch('/some-api', { method: form.method, body: formData });

    // 也可以使用普通的对象：
    const formJson = Object.fromEntries(formData.entries());
    console.log(formJson);
  }

  return (
    <form method="post" onSubmit={handleSubmit}>
      <label>
        贴子标题：<input name="postTitle" defaultValue="骑车" />
      </label>
      <label>
        编辑你的贴子：
        <textarea
          name="postContent"
          defaultValue="我昨天骑车很高兴！"
          rows={4}
          cols={40}
        />
      </label>
      <hr />
      <button type="reset">重新编辑</button>
      <button type="submit">保存贴子</button>
    </form>
  );
}
```
显示更多
### 注意
给 <textarea> 添加 name 属性，例如 <textarea name="postContent" />。指定的 name 将作为表单数据中的一个键，例如 { postContent: "Your post" }。
### 陷阱
默认情况下，<form> 内的任何 <button> 都可以提交表单。这可能会让人感到惊讶！如果你有自定义 Button 组件，请考虑使用 <button type="button"> 而不是 <button>。如果你想要明确指定提交表单的按钮，请使用 <button type="submit">。
### 使用 state 控制文本框
像 <textarea /> 这样的选择框是非受控的。即使你 传递了初始值，比如 <textarea defaultValue="Initial text" />，你的 JSX 也只是指定了初始值，而非当前时刻的值。
如果要渲染一个受控选择框，请传递 value 属性。React 将强制传递 value 属性给文本框。通常，你可以通过声明一个 state 来控制文本框：
```
function NewPost() {  const [postContent, setPostContent] = useState(''); // 声明一个 state 变量...  // ...  return (    <textarea      value={postContent} // ...强制文本框的值与 state 相匹配...      onChange={e => setPostContent(e.target.value)} // ...并在每次改变（change）时更新 state！    />  );}
```
这将帮助你在每次按键时都触发重新渲染。
```
package.jsonApp.jsMarkdownPreview.jspackage.jsonReloadClearFork{
  "dependencies": {
    "react": "latest",
    "react-dom": "latest",
    "react-scripts": "latest",
    "remarkable": "2.0.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject"
  },
  "devDependencies": {}
}
```
### 陷阱
如果传递了 value 但没有传递 onChange，那么将无法在文本框输入任何内容。当你通过传递 value 来控制文本框时，你需要保证文本框始终具有你传递的值。因此，如果你将一个 state 作为 value 传递，但在 onChange 事件处理程序中忘记同步更新该状态变量，React 将在每次插入字符后将选择框恢复到你指定的 value。
## 故障排除
### 输入时文本框没有更新
如果传递了 value 但没有传递 onChange，你将在控制台中看到一个错误：
```
// 🔴 Bug: controlled text area with no onChange handler<textarea value={something} />
```
Console如果在没有提供 onChange 处理程序的情况下向表单字段提供了 value 属性，这将导致文本框只读。如果文本框的内容是可变的，请使用 defaultValue；否则，请指定 onChange 或 readOnly。
正如错误消息所提示的那样，如果你只想 指定初始值，请改为使用 defaultValue：
```
// ✅ Good: uncontrolled text area with an initial value<textarea defaultValue={something} />
```
如果你想 使用 state 控制文本框，请指定 onChange 处理程序：
```
// ✅ Good: controlled text area with onChange<textarea value={something} onChange={e => setSomething(e.target.value)} />
```
如果文本框的内容是只读的，请指定 readOnly 属性：
```
// ✅ Good: readonly controlled text area without on change<textarea value={something} readOnly={true} />
```
### 当我输入时，文本框光标会跳到开头
如果你想要 控制文本框，你应该在 onChange 期间将对应的 state 变量更新为来自 DOM 的文本框的值。
你不应该将它更新为 e.target.value 以外的值：
```
function handleChange(e) {  // 🔴 Bug: updating an input to something other than e.target.value  setFirstName(e.target.value.toUpperCase());}
```
你也不应该异步更新：
```
function handleChange(e) {  // 🔴 Bug: updating an input asynchronously  setTimeout(() => {    setFirstName(e.target.value);  }, 100);}
```
将 state 同步更新 e.target.value 以解决此问题：
```
function handleChange(e) {  // ✅ Updating a controlled input to e.target.value synchronously  setFirstName(e.target.value);}
```
如果这不能解决问题，有可能是因为每次输入时文本框都从 DOM 中删除并重新添加。同样，如果在每次重新渲染时不小心 重置了 state，就会发生这种情况。例如，如果文本框或其祖先组件总是接收不同的 key，或者嵌套使用组件（这在 React 中是不允许的，并且会导致“内部”组件在每次渲染时重新挂载），就会发生这种情况。
### 收到错误：“A component is changing an uncontrolled input to be controlled”
提供的 value 属性必须在整个生命周期中都为字符串。
你不能一会传递 value={undefined} 一会传递 value="some string"，这会导致 React 不清楚你是想指定受控组件还是非受控组件。受控组件的 value 属性应该始终接收字符串，而不是 null 或 undefined。
如果 value 来自 API 或 state，它可能会被初始化为 null 或 undefined。在这种情况下，要么最初将其设置为空字符串（''），要么传递 value={someValue ?? ''} 以确保 value 是一个字符串。