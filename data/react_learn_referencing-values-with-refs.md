学习 React脱围机制 Copy pageCopy
# 使用 ref 引用值
当你希望组件“记住”某些信息，但又不想让这些信息 触发新的渲染 时，你可以使用 ref 。
### 你将会学习到
- 如何向组件添加 ref
- 如何更新 ref 的值
- ref 与 state 有何不同
- 如何安全地使用 ref
## 给你的组件添加 ref
你可以通过从 React 导入 useRef Hook 来为你的组件添加一个 ref：
```
import { useRef } from 'react';
```
在你的组件内，调用 useRef Hook 并传入你想要引用的初始值作为唯一参数。例如，这里的 ref 引用的值是“0”：
```
const ref = useRef(0);
```
useRef 返回一个这样的对象:
```
{  current: 0 // 你向 useRef 传入的值}
```
Rachel Lee Nabors 绘图
你可以用 ref.current 属性访问该 ref 的当前值。这个值是有意被设置为可变的，意味着你既可以读取它也可以写入它。就像一个 React 追踪不到的、用来存储组件信息的秘密“口袋”。（这就是让它成为 React 单向数据流的“脱围机制”的原因 —— 详见下文！）
这里，每次点击按钮时会使 ref.current 递增：
```
App.jsApp.jsReloadClearForkimport { useRef } from 'react';

export default function Counter() {
  let ref = useRef(0);

  function handleClick() {
    ref.current = ref.current + 1;
    alert('你点击了 ' + ref.current + ' 次！');
  }

  return (
    <button onClick={handleClick}>
      点击我！
    </button>
  );
}
```
显示更多
这里的 ref 指向一个数字，但是，像 state 一样，你可以让它指向任何东西：字符串、对象，甚至是函数。与 state 不同的是，ref 是一个普通的 JavaScript 对象，具有可以被读取和修改的 current 属性。
请注意，组件不会在每次递增时重新渲染。 与 state 一样，React 会在每次重新渲染之间保留 ref。但是，设置 state 会重新渲染组件，更改 ref 不会！
## 示例：制作秒表
你可以在单个组件中把 ref 和 state 结合起来使用。例如，让我们制作一个秒表，用户可以通过按按钮来使其启动或停止。为了显示从用户按下“开始”以来经过的时间长度，你需要追踪按下“开始”按钮的时间和当前时间。此信息用于渲染，所以你会把它保存在 state 中：
```
const [startTime, setStartTime] = useState(null);const [now, setNow] = useState(null);
```
当用户按下“开始”时，你将用 setInterval 每 10 毫秒更新一次时间：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Stopwatch() {
  const [startTime, setStartTime] = useState(null);
  const [now, setNow] = useState(null);

  function handleStart() {
    // 开始计时。
    setStartTime(Date.now());
    setNow(Date.now());

    setInterval(() => {
      // 每 10ms 更新一次当前时间。
      setNow(Date.now());
    }, 10);
  }

  let secondsPassed = 0;
  if (startTime != null && now != null) {
    secondsPassed = (now - startTime) / 1000;
  }

  return (
    <>
      <h1>时间过去了： {secondsPassed.toFixed(3)}</h1>
      <button onClick={handleStart}>
        开始
      </button>
    </>
  );
}
```
显示更多
当按下“停止”按钮时，你需要取消现有的 interval，以便让它停止更新 now state 变量。你可以通过调用 clearInterval 来完成此操作。但你需要为其提供 interval ID，此 ID 是之前用户按下 Start、调用 setInterval 时返回的。你需要将 interval ID 保留在某处。 由于 interval ID 不用于渲染，你可以将其保存在 ref 中：
```
App.jsApp.jsReloadClearForkimport { useState, useRef } from 'react';

export default function Stopwatch() {
  const [startTime, setStartTime] = useState(null);
  const [now, setNow] = useState(null);
  const intervalRef = useRef(null);

  function handleStart() {
    setStartTime(Date.now());
    setNow(Date.now());

    clearInterval(intervalRef.current);
    intervalRef.current = setInterval(() => {
      setNow(Date.now());
    }, 10);
  }

  function handleStop() {
    clearInterval(intervalRef.current);
  }

  let secondsPassed = 0;
  if (startTime != null && now != null) {
    secondsPassed = (now - startTime) / 1000;
  }

  return (
    <>
      <h1>时间过去了： {secondsPassed.toFixed(3)}</h1>
      <button onClick={handleStart}>
        开始
      </button>
      <button onClick={handleStop}>
        停止
      </button>
    </>
  );
}
```
显示更多
当一条信息用于渲染时，将它保存在 state 中。当一条信息仅被事件处理器需要，并且更改它不需要重新渲染时，使用 ref 可能会更高效。
## ref 和 state 的不同之处
也许你觉得 ref 似乎没有 state 那样“严格” —— 例如，你可以改变它们而非总是必须使用 state 设置函数。但在大多数情况下，我们建议你使用 state。ref 是一种“脱围机制”，你并不会经常用到它。 以下是 state 和 ref 的对比：
ref |
state |
useRef(initialValue)返回 { current: initialValue } |
useState(initialValue) 返回 state 变量的当前值和一个 state 设置函数 ( [value, setValue]) |
更改时不会触发重新渲染 |
更改时触发重新渲染。 |
可变 —— 你可以在渲染过程之外修改和更新 current 的值。 |
“不可变” —— 你必须使用 state 设置函数来修改 state 变量，从而排队重新渲染。 |
你不应在渲染期间读取（或写入） current 值。 |
你可以随时读取 state。但是，每次渲染都有自己不变的 state 快照。 |
这是一个使用 state 实现的计数器按钮：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      你点击了 {count} 次
    </button>
  );
}
```
因为 count 的值将会被显示，所以为其使用 state 是合理的。当使用 setCount() 设置计数器的值时，React 会重新渲染组件，并且屏幕会更新以展示新的计数。
如果你试图用 ref 来实现它，React 永远不会重新渲染组件，所以你永远不会看到计数变化！看看点击这个按钮如何 不更新它的文本：
```
App.jsApp.jsReloadClearForkimport { useRef } from 'react';

export default function Counter() {
  let countRef = useRef(0);

  function handleClick() {
    // 这样并未重新渲染组件！
    countRef.current = countRef.current + 1;
  }

  return (
    <button onClick={handleClick}>
      你点击了 {countRef.current} 次
    </button>
  );
}
```
显示更多
这就是在渲染期间读取 ref.current 会导致代码不可靠的原因。如果需要，请改用 state。
深入探讨
#### useRef 内部是如何运行的？
显示更多
尽管 useState 和 useRef 都是由 React 提供的，原则上 useRef 可以在 useState 的基础上 实现。 你可以想象在 React 内部，useRef 是这样实现的：
```
// React 内部function useRef(initialValue) {  const [ref, unused] = useState({ current: initialValue });  return ref;}
```
第一次渲染期间，useRef 返回 { current: initialValue }。 该对象由 React 存储，因此在下一次渲染期间将返回相同的对象。 请注意，在这个示例中，state 设置函数没有被用到。它是不必要的，因为 useRef 总是需要返回相同的对象！
React 提供了一个内置版本的 useRef，因为它在实践中很常见。 但是你可以将其视为没有设置函数的常规 state 变量。 如果你熟悉面向对象编程，ref 可能会让你想起实例字段 —— 但是你写的不是 this.something，而是 somethingRef.current。
## 何时使用 ref
通常，当你的组件需要“跳出” React 并与外部 API 通信时，你会用到 ref —— 通常是不会影响组件外观的浏览器 API。以下是这些罕见情况中的几个：
- 存储 timeout ID
- 存储和操作 DOM 元素，我们将在 下一页 中介绍
- 存储不需要被用来计算 JSX 的其他对象。
如果你的组件需要存储一些值，但不影响渲染逻辑，请选择 ref。
## ref 的最佳实践
遵循这些原则将使你的组件更具可预测性：
- 将 ref 视为脱围机制。当你使用外部系统或浏览器 API 时，ref 很有用。如果你很大一部分应用程序逻辑和数据流都依赖于 ref，你可能需要重新考虑你的方法。
- 不要在渲染过程中读取或写入 ref.current。 如果渲染过程中需要某些信息，请使用 state 代替。由于 React 不知道 ref.current 何时发生变化，即使在渲染时读取它也会使组件的行为难以预测。（唯一的例外是像 if (!ref.current) ref.current = new Thing() 这样的代码，它只在第一次渲染期间设置一次 ref。）
React state 的限制不适用于 ref。例如，state 就像 每次渲染的快照，并且 不会同步更新。但是当你改变 ref 的 current 值时，它会立即改变：
```
ref.current = 5;console.log(ref.current); // 5
```
这是因为 ref 本身是一个普通的 JavaScript 对象， 所以它的行为就像对象那样。
当你使用 ref 时，也无需担心 避免变更。只要你改变的对象不用于渲染，React 就不会关心你对 ref 或其内容做了什么。
## ref 和 DOM
你可以将 ref 指向任何值。但是，ref 最常见的用法是访问 DOM 元素。例如，如果你想以编程方式聚焦一个输入框，这种用法就会派上用场。当你将 ref 传递给 JSX 中的 ref 属性时，比如 <div ref={myRef}>，React 会将相应的 DOM 元素放入 myRef.current 中。当元素从 DOM 中删除时，React 会将 myRef.current 更新为 null。你可以在 使用 ref 操作 DOM 中阅读更多相关信息。
## 摘要
- ref 是一种脱围机制，用于保留不用于渲染的值。 你不会经常需要它们。
- ref 是一个普通的 JavaScript 对象，具有一个名为 current 的属性，你可以对其进行读取或设置。
- 你可以通过调用 useRef Hook 来让 React 给你一个 ref。
- 与 state 一样，ref 允许你在组件的重新渲染之间保留信息。
- 与 state 不同，设置 ref 的 current 值不会触发重新渲染。
- 不要在渲染过程中读取或写入 ref.current。这使你的组件难以预测。
## 尝试一些挑战
1. 修复坏掉的聊天输入框 2. 修复无法重新渲染的组件 3. 修复防抖 4. 读取最新的 state
#### 第 1 个挑战 共 4 个挑战: 修复坏掉的聊天输入框
输入消息并单击“发送”。你会注意到，在看到“已发送！”提示框之前有 3 秒的延迟。在此延迟期间，你可以看到一个“撤消”按钮。点击它。这个“撤消”按钮应该阻止“发送！”消息弹出。它通过调用 clearTimeout 来做到这点，这一步骤需要使用在 handleSend 时保存的 timeout ID。但是，即使在单击“撤消”后，“已发送！”消息仍然出现。找出它不起作用的原因，然后修复它。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Chat() {
  const [text, setText] = useState('');
  const [isSending, setIsSending] = useState(false);
  let timeoutID = null;

  function handleSend() {
    setIsSending(true);
    timeoutID = setTimeout(() => {
      alert('已发送！');
      setIsSending(false);
    }, 3000);
  }

  function handleUndo() {
    setIsSending(false);
    clearTimeout(timeoutID);
  }

  return (
    <>
      <input
        disabled={isSending}
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <button
        disabled={isSending}
        onClick={handleSend}>
        {isSending ? '发送中……' : '发送'}
      </button>
      {isSending &&
        <button onClick={handleUndo}>
          撤销
        </button>
      }
    </>
  );
}
```