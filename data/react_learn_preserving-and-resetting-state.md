学习 React状态管理 Copy pageCopy
# 对 state 进行保留和重置
各个组件的 state 是各自独立的。根据组件在 UI 树中的位置，React 可以跟踪哪些 state 属于哪个组件。你可以控制在重新渲染过程中何时对 state 进行保留和重置。
### 你将会学习到
- React 何时选择保留或重置状态
- 如何强制 React 重置组件的状态
- 键和类型如何影响状态是否被保留
## 状态与渲染树中的位置相关
React 会为 UI 中的组件结构构建 渲染树。
当向一个组件添加状态时，那么可能会认为状态“存在”在组件内。但实际上，状态是由 React 保存的。React 通过组件在渲染树中的位置将它保存的每个状态与正确的组件关联起来。
下面的例子中只有一个 <Counter /> JSX 标签，但它会在两个不同的位置渲染：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  const counter = <Counter />;
  return (
    <div>
      {counter}
      {counter}
    </div>
  );
}

function Counter() {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
下面是它们的树形结构的样子：
React 树
这是两个独立的 counter，因为它们在树中被渲染在了各自的位置。 一般情况下你不用去考虑这些位置来使用 React，但知道它们是如何工作会很有用。
在 React 中，屏幕中的每个组件都有完全独立的 state。举个例子，当你并排渲染两个 Counter 组件时，它们都会拥有各自独立的 score 和 hover state。
试试点击两个 counter 你会发现它们互不影响：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  return (
    <div>
      <Counter />
      <Counter />
    </div>
  );
}

function Counter() {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
如你所见，当一个计数器被更新时，只有该组件的状态会被更新：
Updating state
只有当在树中相同的位置渲染相同的组件时，React 才会一直保留着组件的 state。想要验证这一点，可以将两个计数器的值递增，取消勾选 “渲染第二个计数器” 复选框，然后再次勾选它：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  const [showB, setShowB] = useState(true);
  return (
    <div>
      <Counter />
      {showB && <Counter />}
      <label>
        <input
          type="checkbox"
          checked={showB}
          onChange={e => {
            setShowB(e.target.checked)
          }}
        />
        渲染第二个计数器
      </label>
    </div>
  );
}

function Counter() {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
注意，当你停止渲染第二个计数器的那一刻，它的 state 完全消失了。这是因为 React 在移除一个组件时，也会销毁它的 state。
删除组件
当你重新勾选“渲染第二个计数器”复选框时，另一个计数器及其 state 将从头开始初始化（score = 0）并被添加到 DOM 中。
添加组件
只要一个组件还被渲染在 UI 树的相同位置，React 就会保留它的 state。 如果它被移除，或者一个不同的组件被渲染在相同的位置，那么 React 就会丢掉它的 state。
## 相同位置的相同组件会使得 state 被保留下来
在这个例子中，有两个不同的 <Counter /> 标签：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  const [isFancy, setIsFancy] = useState(false);
  return (
    <div>
      {isFancy ? (
        <Counter isFancy={true} />
      ) : (
        <Counter isFancy={false} />
      )}
      <label>
        <input
          type="checkbox"
          checked={isFancy}
          onChange={e => {
            setIsFancy(e.target.checked)
          }}
        />
        使用好看的样式
      </label>
    </div>
  );
}

function Counter({ isFancy }) {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }
  if (isFancy) {
    className += ' fancy';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
当你勾选或清空复选框的时候，计数器 state 并没有被重置。不管 isFancy 是 true 还是 false，根组件 App 返回的 div 的第一个子组件都是 <Counter />：
更新 App 的状态不会重置 Counter，因为 Counter 始终保持在同一位置。
它是位于相同位置的相同组件，所以对 React 来说，它是同一个计数器。
### 陷阱
记住 对 React 来说重要的是组件在 UI 树中的位置,而不是在 JSX 中的位置！ 这个组件在 if 内外有两个return 语句，它们带有不同的 <Counter /> JSX 标签：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  const [isFancy, setIsFancy] = useState(false);
  if (isFancy) {
    return (
      <div>
        <Counter isFancy={true} />
        <label>
          <input
            type="checkbox"
            checked={isFancy}
            onChange={e => {
              setIsFancy(e.target.checked)
            }}
          />
          使用好看的样式
        </label>
      </div>
    );
  }
  return (
    <div>
      <Counter isFancy={false} />
      <label>
        <input
          type="checkbox"
          checked={isFancy}
          onChange={e => {
            setIsFancy(e.target.checked)
          }}
        />
        使用好看的样式
      </label>
    </div>
  );
}

function Counter({ isFancy }) {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }
  if (isFancy) {
    className += ' fancy';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
你可能以为当你勾选复选框的时候 state 会被重置，但它并没有！这是因为 两个 <Counter /> 标签被渲染在了相同的位置。 React 不知道你的函数里是如何进行条件判断的，它只会“看到”你返回的树。
在这两种情况下，App 组件都会返回一个包裹着 <Counter /> 作为第一个子组件的 div。这就是 React 认为它们是 同一个 <Counter /> 的原因。你可以认为它们有相同的“地址”：根组件的第一个子组件的第一个子组件。不管你的逻辑是怎么组织的，这就是 React 在前后两次渲染之间将它们进行匹配的方式。
## 相同位置的不同组件会使 state 重置
在这个例子中，勾选复选框会将 <Counter> 替换为一个 <p>：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  const [isPaused, setIsPaused] = useState(false);
  return (
    <div>
      {isPaused ? (
        <p>待会见！</p>
      ) : (
        <Counter />
      )}
      <label>
        <input
          type="checkbox"
          checked={isPaused}
          onChange={e => {
            setIsPaused(e.target.checked)
          }}
        />
        休息一下
      </label>
    </div>
  );
}

function Counter() {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
示例中，你在相同位置对 不同 的组件类型进行切换。刚开始 <div> 的第一个子组件是一个 Counter。但是当你切换成 p 时，React 将 Counter 从 UI 树中移除了并销毁了它的状态。
当 Counter 变为 p 时，Counter 会被移除，同时 p 被添加。
当切换回来时，p 会被删除，而 Counter 会被添加
并且，当你在相同位置渲染不同的组件时，组件的整个子树都会被重置。要验证这一点，可以增加计数器的值然后勾选复选框：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  const [isFancy, setIsFancy] = useState(false);
  return (
    <div>
      {isFancy ? (
        <div>
          <Counter isFancy={true} />
        </div>
      ) : (
        <section>
          <Counter isFancy={false} />
        </section>
      )}
      <label>
        <input
          type="checkbox"
          checked={isFancy}
          onChange={e => {
            setIsFancy(e.target.checked)
          }}
        />
        使用好看的样式
      </label>
    </div>
  );
}

function Counter({ isFancy }) {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }
  if (isFancy) {
    className += ' fancy';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
当你勾选复选框后计数器的 state 被重置了。虽然你渲染了一个 Counter，但是 div 的第一个子组件从 section 变成了 div。当子组件 section 从 DOM 中被移除的时候，它底下的整棵树（包含 Counter 以及它的 state）也都被销毁了。
当 section 变为 div 时，section 会被删除，新的 div 被添加
当切换回来时，div 会被删除，新的 section 被添加
一般来说，如果你想在重新渲染时保留 state，几次渲染中的树形结构就应该相互“匹配”。结构不同就会导致 state 的销毁，因为 React 会在将一个组件从树中移除时销毁它的 state。
### 陷阱
以下是你不应该把组件函数的定义嵌套起来的原因。
示例中， MyTextField 组件被定义在 MyComponent 内部：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function MyComponent() {
  const [counter, setCounter] = useState(0);

  function MyTextField() {
    const [text, setText] = useState('');

    return (
      <input
        value={text}
        onChange={e => setText(e.target.value)}
      />
    );
  }

  return (
    <>
      <MyTextField />
      <button onClick={() => {
        setCounter(counter + 1)
      }}>点击了 {counter} 次</button>
    </>
  );
}
```
显示更多
每次你点击按钮，输入框的 state 都会消失！这是因为每次 MyComponent 渲染时都会创建一个 不同 的 MyTextField 函数。你在相同位置渲染的是 不同 的组件，所以 React 将其下所有的 state 都重置了。这样会导致 bug 以及性能问题。为了避免这个问题， 永远要将组件定义在最上层并且不要把它们的定义嵌套起来。
## 在相同位置重置 state
默认情况下，React 会在一个组件保持在同一位置时保留它的 state。通常这就是你想要的，所以把它作为默认特性很合理。但有时候，你可能想要重置一个组件的 state。考虑一下这个应用，它可以让两个玩家在每个回合中记录他们的得分：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Scoreboard() {
  const [isPlayerA, setIsPlayerA] = useState(true);
  return (
    <div>
      {isPlayerA ? (
        <Counter person="Taylor" />
      ) : (
        <Counter person="Sarah" />
      )}
      <button onClick={() => {
        setIsPlayerA(!isPlayerA);
      }}>
        下一位玩家！
      </button>
    </div>
  );
}

function Counter({ person }) {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{person} 的分数：{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
目前当你切换玩家时，分数会被保留下来。这两个 Counter 出现在相同的位置，所以 React 会认为它们是 同一个 Counter，只是传了不同的 person prop。
但是从概念上讲，这个应用中的两个计数器应该是各自独立的。虽然它们在 UI 中的位置相同，但是一个是 Taylor 的计数器，一个是 Sarah 的计数器。
有两个方法可以在它们相互切换时重置 state：
- 将组件渲染在不同的位置
- 使用 key 赋予每个组件一个明确的身份
### 方法一：将组件渲染在不同的位置
你如果想让两个 Counter 各自独立的话，可以将它们渲染在不同的位置：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Scoreboard() {
  const [isPlayerA, setIsPlayerA] = useState(true);
  return (
    <div>
      {isPlayerA &&
        <Counter person="Taylor" />
      }
      {!isPlayerA &&
        <Counter person="Sarah" />
      }
      <button onClick={() => {
        setIsPlayerA(!isPlayerA);
      }}>
        下一位玩家！
      </button>
    </div>
  );
}

function Counter({ person }) {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{person} 的分数：{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
- 起初 isPlayerA 的值是 true。所以第一个位置包含了 Counter 的 state，而第二个位置是空的。
- 当你点击“下一位玩家”按钮时，第一个位置会被清空，而第二个位置现在包含了一个 Counter。
Initial state
Clicking “next”
Clicking “next” again
每当 Counter 组件从 DOM 中移除时，它的 state 会被销毁。这就是每次点击按钮它们就会被重置的原因。
这个解决方案在你只有少数几个独立的组件渲染在相同的位置时会很方便。这个例子中只有 2 个组件，所以在 JSX 里将它们分开进行渲染并不麻烦。
### 方法二：使用 key 来重置 state
还有另一种更通用的重置组件 state 的方法。
你可能在 渲染列表 时见到过 key。但 key 不只可以用于列表！你可以使用 key 来让 React 区分任何组件。默认情况下，React 使用父组件内部的顺序（“第一个计数器”、“第二个计数器”）来区分组件。但是 key 可以让你告诉 React 这不仅仅是 第一个 或者 第二个 计数器，而且还是一个特定的计数器——例如，Taylor 的 计数器。这样无论它出现在树的任何位置， React 都会知道它是 Taylor 的 计数器！
在这个例子中，即使两个 <Counter /> 会出现在 JSX 中的同一个位置，它们也不会共享 state：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Scoreboard() {
  const [isPlayerA, setIsPlayerA] = useState(true);
  return (
    <div>
      {isPlayerA ? (
        <Counter key="Taylor" person="Taylor" />
      ) : (
        <Counter key="Sarah" person="Sarah" />
      )}
      <button onClick={() => {
        setIsPlayerA(!isPlayerA);
      }}>
        下一位玩家！
      </button>
    </div>
  );
}

function Counter({ person }) {
  const [score, setScore] = useState(0);
  const [hover, setHover] = useState(false);

  let className = 'counter';
  if (hover) {
    className += ' hover';
  }

  return (
    <div
      className={className}
      onPointerEnter={() => setHover(true)}
      onPointerLeave={() => setHover(false)}
    >
      <h1>{person} 的分数：{score}</h1>
      <button onClick={() => setScore(score + 1)}>
        加一
      </button>
    </div>
  );
}
```
显示更多
在 Taylor 和 Sarah 之间切换不会使 state 被保留下来。因为 你给他们赋了不同的 key：
```
{isPlayerA ? (  <Counter key="Taylor" person="Taylor" />) : (  <Counter key="Sarah" person="Sarah" />)}
```
指定一个 key 能够让 React 将 key 本身而非它们在父组件中的顺序作为位置的一部分。这就是为什么尽管你用 JSX 将组件渲染在相同位置，但在 React 看来它们是两个不同的计数器。因此它们永远都不会共享 state。每当一个计数器出现在屏幕上时，它的 state 会被创建出来。每当它被移除时，它的 state 就会被销毁。在它们之间切换会一次又一次地使它们的 state 重置。
### 注意
请记住 key 不是全局唯一的。它们只能指定 父组件内部 的顺序。
### 使用 key 重置表单
使用 key 来重置 state 在处理表单时特别有用。
在这个聊天应用中， <Chat> 组件包含文本输入 state：
```
App.jsContactList.jsChat.jsApp.jsReloadClearForkimport { useState } from 'react';
import Chat from './Chat.js';
import ContactList from './ContactList.js';

export default function Messenger() {
  const [to, setTo] = useState(contacts[0]);
  return (
    <div>
      <ContactList
        contacts={contacts}
        selectedContact={to}
        onSelect={contact => setTo(contact)}
      />
      <Chat contact={to} />
    </div>
  )
}

const contacts = [
  { id: 0, name: 'Taylor', email: 'taylor@mail.com' },
  { id: 1, name: 'Alice', email: 'alice@mail.com' },
  { id: 2, name: 'Bob', email: 'bob@mail.com' }
];
```
显示更多
尝试在输入框中输入一些内容，然后点击 “Alice” 或 “Bob” 来选择不同的收件人。你会发现因为 <Chat> 被渲染在了树的相同位置，输入框的 state 被保留下来了。
在很多应用里这可能会是大家所需要的特性，但在这个聊天应用里并不是！ 你不应该让用户因为一次偶然的点击而把他们已经输入的信息发送给一个错误的人。要修复这个问题，只需给组件添加一个 key ：
```
<Chat key={to.id} contact={to} />
```
这样确保了当你选择一个不同的收件人时， Chat 组件——包括其下方树中的任何 state——都将从头开始重新创建。 React 还将重新创建 DOM 元素，而不是复用它们。
现在切换收件人就总会清除文本字段了：
```
App.jsContactList.jsChat.jsApp.jsReloadClearForkimport { useState } from 'react';
import Chat from './Chat.js';
import ContactList from './ContactList.js';

export default function Messenger() {
  const [to, setTo] = useState(contacts[0]);
  return (
    <div>
      <ContactList
        contacts={contacts}
        selectedContact={to}
        onSelect={contact => setTo(contact)}
      />
      <Chat key={to.id} contact={to} />
    </div>
  )
}

const contacts = [
  { id: 0, name: 'Taylor', email: 'taylor@mail.com' },
  { id: 1, name: 'Alice', email: 'alice@mail.com' },
  { id: 2, name: 'Bob', email: 'bob@mail.com' }
];
```
显示更多
深入探讨
#### 为被移除的组件保留 state
显示更多
在真正的聊天应用中，你可能会想在用户再次选择前一个收件人时恢复输入 state。对于一个不可见的组件，有几种方法可以让它的 state “活下去”：
- 与其只渲染现在这一个聊天，你可以把 所有 聊天都渲染出来，但用 CSS 把其他聊天隐藏起来。这些聊天就不会从树中被移除了，所以它们的内部 state 会被保留下来。这种解决方法对于简单 UI 非常有效。但如果要隐藏的树形结构很大且包含了大量的 DOM 节点，那么性能就会变得很差。
- 你可以进行 状态提升 并在父组件中保存每个收件人的草稿消息。这样即使子组件被移除了也无所谓，因为保留重要信息的是父组件。这是最常见的解决方法。
- 除了 React 的 state，你也可以使用其他数据源。例如，也许你希望即使用户不小心关闭页面也可以保存一份信息草稿。要实现这一点，你可以让 Chat 组件通过读取 localStorage 对其 state 进行初始化，并把草稿保存在那里。
无论采取哪种策略，与 Alice 的聊天在概念上都不同于 与 Bob 的聊天，因此根据当前收件人为 <Chat> 树指定一个 key 是合理的。
## 摘要
- 只要在相同位置渲染的是相同组件， React 就会保留状态。
- state 不会被保存在 JSX 标签里。它与你在树中放置该 JSX 的位置相关联。
- 你可以通过为一个子树指定一个不同的 key 来重置它的 state。
- 不要嵌套组件的定义，否则你会意外地导致 state 被重置。
## 尝试一些挑战
1. 修复丢失的输入框文本 2. 交换两个表单字段 3. 重置详情表单 4. 清除正在加载的图片 5. 修复列表中错位的 state
#### 第 1 个挑战 共 5 个挑战: 修复丢失的输入框文本
这个例子在你按下按钮时会展示一条消息，但同时也会意外地重置输入框。为什么会发生这种情况？修复它，使按下按钮不再导致输入框文本重置。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function App() {
  const [showHint, setShowHint] = useState(false);
  if (showHint) {
    return (
      <div>
        <p><i>提示：你最喜欢的城市？</i></p>
        <Form />
        <button onClick={() => {
          setShowHint(false);
        }}>隐藏提示</button>
      </div>
    );
  }
  return (
    <div>
      <Form />
      <button onClick={() => {
        setShowHint(true);
      }}>显示提示</button>
    </div>
  );
}

function Form() {
  const [text, setText] = useState('');
  return (
    <textarea
      value={text}
      onChange={e => setText(e.target.value)}
    />
  );
}
```