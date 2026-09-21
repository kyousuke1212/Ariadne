API 参考Hook Copy pageCopy
# useDeferredValue
useDeferredValue 是一个 React Hook，可以让你延迟更新 UI 的某些部分。
```
const deferredValue = useDeferredValue(value)
```
参考
- useDeferredValue(value, initialValue?)
用法
- 在新内容加载期间显示旧内容。
- 表明内容已过时
- 延迟渲染 UI 的某些部分
## 参考
### useDeferredValue(value, initialValue?)
在组件的顶层调用 useDeferredValue 来获取该值的延迟版本。
```
import { useState, useDeferredValue } from 'react';function SearchPage() {  const [query, setQuery] = useState('');  const deferredQuery = useDeferredValue(query);  // ...}
```
请看下方更多示例。
#### 参数
- value: 你想延迟的值，可以是任何类型。
- 可选的 initialValue: 组件初始渲染时使用的值。如果省略此选项，useDeferredValue 在初始渲染期间不会延迟，因为没有以前的版本可以渲染。
#### 返回值
- currentValue: 在初始渲染期间，返回的延迟值是 initialValue 或你提供的值。在更新期间，React 首先尝试使用旧值重新渲染（因此返回旧值），然后在后台尝试使用新值重新渲染（因此返回更新后的值）。
#### 注意事项
当更新发生在 Transition 内部时，useDeferredValue 总是返回新的 value 并且不会产生延迟渲染，因为该更新已经被延迟了。
传递给 useDeferredValue 的值应该是原始值（如字符串和数字）或是在渲染之外创建的对象。如果你在渲染期间创建一个新对象并立即将其传递给 useDeferredValue，它在每次渲染时都会不同，从而导致不必要的后台重新渲染。
当 useDeferredValue 接收到与之前不同的值（使用 Object.is 进行比较）时，除了当前渲染（此时它仍然使用旧值），它还会安排一个后台重新渲染。这个后台重新渲染是可以被中断的，如果 value 有新的更新，React 会从头开始重新启动后台渲染。举个例子，如果用户在输入框中的输入速度比接收延迟值的图表重新渲染的速度快，那么图表只会在用户停止输入后重新渲染。
useDeferredValue 与 <Suspense> 集成。如果由于新值引起的后台更新导致 UI 暂停，用户将不会看到后备方案。他们将看到旧的延迟值，直到数据加载完成。
useDeferredValue 本身并不能阻止额外的网络请求。
useDeferredValue 本身不会引起任何固定的延迟。一旦 React 完成原始的重新渲染，它会立即开始使用新的延迟值处理后台重新渲染。由事件（例如输入）引起的任何更新都会中断后台重新渲染，并被优先处理。
由 useDeferredValue 引起的后台重新渲染在提交到屏幕之前不会触发 Effect。如果后台重新渲染被暂停，Effect 将在数据加载后和 UI 更新后运行。
## 用法
### 在新内容加载期间显示旧内容。
在组件的顶层调用 useDeferredValue 来延迟更新 UI 的某些部分。
```
import { useState, useDeferredValue } from 'react';function SearchPage() {  const [query, setQuery] = useState('');  const deferredQuery = useDeferredValue(query);  // ...}
```
在初始渲染期间，返回的 延迟值 与你提供的 值 相同。
在更新期间，延迟值 会“滞后于”最新的 值。具体地说，React 首先会在不更新延迟值的情况下进行重新渲染，然后在后台尝试使用新接收到的值进行重新渲染。
让我们通过一个例子来看看什么时候该使用它。
### 注意
这个例子假设你使用了支持 Suspense 的数据源：
- 使用支持 suspense 的框架进行数据获取，例如 Relay 和 Next.js
- 使用 lazy 懒加载组件代码
- 使用 use 读取 Promise 的值
了解更多有关 suspense 及其限制的信息。
这个例子中，在获取搜索结果时，SearchResults 组件会 suspend。尝试输入 "a"，等待结果出现后，将其编辑为 "ab"。此时 "a" 的结果会被加载中的后备方案替代。
```
App.jsSearchResults.jsApp.jsReloadClearForkimport { Suspense, useState } from 'react';
import SearchResults from './SearchResults.js';

export default function App() {
  const [query, setQuery] = useState('');
  return (
    <>
      <label>
        Search albums:
        <input value={query} onChange={e => setQuery(e.target.value)} />
      </label>
      <Suspense fallback={<h2>Loading...</h2>}>
        <SearchResults query={query} />
      </Suspense>
    </>
  );
}
```
显示更多
一个常见的备选 UI 模式是 延迟 更新结果列表，并继续显示之前的结果，直到新的结果准备好。调用 useDeferredValue 并将延迟版本的查询参数向下传递：
```
export default function App() {  const [query, setQuery] = useState('');  const deferredQuery = useDeferredValue(query);  return (    <>      <label>        Search albums:        <input value={query} onChange={e => setQuery(e.target.value)} />      </label>      <Suspense fallback={<h2>Loading...</h2>}>        <SearchResults query={deferredQuery} />      </Suspense>    </>  );}
```
query 会立即更新，所以输入框将显示新值。然而，deferredQuery 在数据加载完成前会保留以前的值，因此 SearchResults 将暂时显示旧的结果。
在下面的示例中，输入 "a"，等待结果加载完成，然后将输入框编辑为 "ab"。注意，现在你看到的不是 suspense 后备方案，而是旧的结果列表，直到新的结果加载完成：
```
App.jsSearchResults.jsApp.jsReloadClearForkimport { Suspense, useState, useDeferredValue } from 'react';
import SearchResults from './SearchResults.js';

export default function App() {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  return (
    <>
      <label>
        Search albums:
        <input value={query} onChange={e => setQuery(e.target.value)} />
      </label>
      <Suspense fallback={<h2>Loading...</h2>}>
        <SearchResults query={deferredQuery} />
      </Suspense>
    </>
  );
}
```
显示更多
深入探讨
#### 如何在内部实现延迟值？
显示更多
你可以将其看成两个步骤：
首先，React 会使用新的 query 值（"ab"）和旧的 deferredQuery 值（仍为 "a"）重新渲染。 传递给结果列表的 deferredQuery 值是 延迟 的，它“滞后于” query 值。
在后台，React 尝试重新渲染，并将 query 和 deferredQuery 两个值都更新为 "ab"。 如果此次重新渲染完成，React 将在屏幕上显示它。但是，如果它 suspense（即 "ab" 的结果尚未加载），React 将放弃这次渲染，并在数据加载后再次尝试重新渲染。用户将一直看到旧的延迟值，直到数据准备就绪。
被推迟的“后台”渲染是可中断的。例如，如果你再次在输入框中输入，React 将会中断渲染，并从新值开始重新渲染。React 总是使用最新提供的值。
注意，每次按键仍会发起一个网络请求。这里延迟的是显示结果（直到它们准备就绪），而不是网络请求本身。即使用户继续输入，每个按键的响应都会被缓存，所以按下 Backspace 键是瞬时的，不会再次获取数据。
### 表明内容已过时
在上面的示例中，当最新的查询结果仍在加载时，没有任何提示。如果新的结果需要一段时间才能加载完成，这可能会让用户感到困惑。为了更明显地告知用户结果列表与最新查询不匹配，你可以在显示旧的查询结果时添加一个视觉提示：
```
<div style={{  opacity: query !== deferredQuery ? 0.5 : 1,}}>  <SearchResults query={deferredQuery} /></div>
```
有了上面这段代码，当你开始输入时，旧的结果列表会略微变暗，直到新的结果列表加载完毕。你也可以添加 CSS 过渡来延迟变暗的过程，让用户感受到一种渐进式的过渡，就像下面的例子一样：
```
App.jsSearchResults.jsApp.jsReloadClearForkimport { Suspense, useState, useDeferredValue } from 'react';
import SearchResults from './SearchResults.js';

export default function App() {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;
  return (
    <>
      <label>
        Search albums:
        <input value={query} onChange={e => setQuery(e.target.value)} />
      </label>
      <Suspense fallback={<h2>Loading...</h2>}>
        <div style={{
          opacity: isStale ? 0.5 : 1,
          transition: isStale ? 'opacity 0.2s 0.2s linear' : 'opacity 0s 0s linear'
        }}>
          <SearchResults query={deferredQuery} />
        </div>
      </Suspense>
    </>
  );
}
```
显示更多
### 延迟渲染 UI 的某些部分
你还可以将 useDeferredValue 作为性能优化的手段。当你的 UI 某个部分重新渲染很慢、没有简单的优化方法，同时你又希望避免它阻塞其他 UI 的渲染时，使用 useDeferredValue 很有帮助。
想象一下，你有一个文本框和一个组件（例如图表或长列表），在每次按键时都会重新渲染：
```
function App() {  const [text, setText] = useState('');  return (    <>      <input value={text} onChange={e => setText(e.target.value)} />      <SlowList text={text} />    </>  );}
```
首先，我们可以优化 SlowList，使其在 props 不变的情况下跳过重新渲染。只需将其 用 memo 包裹 即可：
```
const SlowList = memo(function SlowList({ text }) {  // ...});
```
然而，这仅在 SlowList 的 props 与上一次的渲染时相同才有用。你现在遇到的问题是，当这些 props 不同 时，并且实际上需要展示不同的视觉输出时，页面会变得很慢。
具体而言，主要的性能问题在于，每次你输入内容时，SlowList 都会接收新的 props，并重新渲染整个树结构，这会让输入感觉很卡顿。使用 useDeferredValue 能够优先更新输入框（必须快速更新），而不是更新结果列表（可以更新慢一些），从而缓解这个问题：
```
function App() {  const [text, setText] = useState('');  const deferredText = useDeferredValue(text);  return (    <>      <input value={text} onChange={e => setText(e.target.value)} />      <SlowList text={deferredText} />    </>  );}
```
这并没有让 SlowList 的重新渲染变快。然而，它告诉 React 可以将列表的重新渲染优先级降低，这样就不会阻塞按键输入。列表的更新会“滞后”于输入，然后“追赶”上来。与之前一样，React 会尽快更新列表，但不会阻塞用户输入。
#### useDeferredValue 和未优化的重新渲染之间的区别
1. 延迟列表的重新渲染 2. 列表的未优化重新渲染
#### 第 1 个示例 共 2 个示例: 延迟列表的重新渲染
在这个例子中，SlowList 组件中的每个 item 都被 故意减缓了渲染速度，这样你就可以看到 useDeferredValue 是如何让输入保持响应的。当你在输入框中输入时，你会发现输入很灵敏，而列表的更新会稍有延迟。
```
App.jsSlowList.jsApp.jsReloadClearForkimport { useState, useDeferredValue } from 'react';
import SlowList from './SlowList.js';

export default function App() {
  const [text, setText] = useState('');
  const deferredText = useDeferredValue(text);
  return (
    <>
      <input value={text} onChange={e => setText(e.target.value)} />
      <SlowList text={deferredText} />
    </>
  );
}
```
下一个示例
### 陷阱
这个优化需要将 SlowList 包裹在 memo 中。这是因为每当 text 改变时，React 需要能够快速重新渲染父组件。在重新渲染期间，deferredText 仍然保持着之前的值，因此 SlowList 可以跳过重新渲染（它的 props 没有改变）。如果没有 memo，SlowList 仍会重新渲染，这将使优化失去意义。
深入探讨
#### 延迟一个值与防抖和节流之间有什么不同？
显示更多
在上述的情景中，你可能会使用这两种常见的优化技术：
- 防抖 是指在用户停止输入一段时间（例如一秒钟）之后再更新列表。
- 节流 是指每隔一段时间（例如最多每秒一次）更新列表。
虽然这些技术在某些情况下是有用的，但 useDeferredValue 更适合优化渲染，因为它与 React 自身深度集成，并且能够适应用户的设备。
与防抖或节流不同，useDeferredValue 不需要选择任何固定延迟时间。如果用户的设备很快（比如性能强劲的笔记本电脑），延迟的重渲染几乎会立即发生并且不会被察觉。如果用户的设备较慢，那么列表会相应地“滞后”于输入，滞后的程度与设备的速度有关。
此外，与防抖或节流不同，useDeferredValue 执行的延迟重新渲染默认是可中断的。这意味着，如果 React 正在重新渲染一个大型列表，但用户进行了另一次键盘输入，React 会放弃该重新渲染，先处理键盘输入，然后再次开始在后台渲染。相比之下，防抖和节流仍会产生不顺畅的体验，因为它们是阻塞的：它们仅仅是将渲染阻塞键盘输入的时刻推迟了。
如果你要优化的工作不是在渲染期间发生的，那么防抖和节流仍然非常有用。例如，它们可以让你减少网络请求的次数。你也可以同时使用这些技术。