学习 React状态管理 Copy pageCopy
# 选择 State 结构
构建良好的 state 可以让组件变得易于修改和调试，而不会经常出错。以下是你在构建 state 时应该考虑的一些建议。
### 你将会学习到
- 使用单个 state 变量还是多个 state 变量
- 组织 state 时应避免的内容
- 如何解决 state 结构中的常见问题
## 构建 state 的原则
当你编写一个存有 state 的组件时，你需要选择使用多少个 state 变量以及它们都是怎样的数据格式。尽管选择次优的 state 结构下也可以编写正确的程序，但有几个原则可以指导你做出更好的决策：
- 合并关联的 state。如果你总是同时更新两个或更多的 state 变量，请考虑将它们合并为一个单独的 state 变量。
- 避免互相矛盾的 state。当 state 结构中存在多个相互矛盾或“不一致”的 state 时，你就可能为此会留下隐患。应尽量避免这种情况。
- 避免冗余的 state。如果你能在渲染期间从组件的 props 或其现有的 state 变量中计算出一些信息，则不应将这些信息放入该组件的 state 中。
- 避免重复的 state。当同一数据在多个 state 变量之间或在多个嵌套对象中重复时，这会很难保持它们同步。应尽可能减少重复。
- 避免深度嵌套的 state。深度分层的 state 更新起来不是很方便。如果可能的话，最好以扁平化方式构建 state。
这些原则背后的目标是 使 state 易于更新而不引入错误。从 state 中删除冗余和重复数据有助于确保所有部分保持同步。这类似于数据库工程师想要 “规范化”数据库结构，以减少出现错误的机会。用爱因斯坦的话说，“让你的状态尽可能简单，但不要过于简单。”
现在让我们来看看这些原则在实际中是如何应用的。
## 合并关联的 state
有时候你可能会不确定是使用单个 state 变量还是多个 state 变量。
你会像下面这样做吗？
```
const [x, setX] = useState(0);const [y, setY] = useState(0);
```
或这样？
```
const [position, setPosition] = useState({ x: 0, y: 0 });
```
从技术上讲，你可以使用其中任何一种方法。但是，如果某两个 state 变量总是一起变化，则将它们统一成一个 state 变量可能更好。这样你就不会忘记让它们始终保持同步，就像下面这个例子中，移动光标会同时更新红点的两个坐标：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function MovingDot() {
  const [position, setPosition] = useState({
    x: 0,
    y: 0
  });
  return (
    <div
      onPointerMove={e => {
        setPosition({
          x: e.clientX,
          y: e.clientY
        });
      }}
      style={{
        position: 'relative',
        width: '100vw',
        height: '100vh',
      }}>
      <div style={{
        position: 'absolute',
        backgroundColor: 'red',
        borderRadius: '50%',
        transform: `translate(${position.x}px, ${position.y}px)`,
        left: -10,
        top: -10,
        width: 20,
        height: 20,
      }} />
    </div>
  )
}
```
显示更多
另一种你需要将数据整合到一个对象或一个数组的情况是，你不知道未来需要多少个 state 片段。例如，有一个用户可以添加自定义字段的表单时，这将会很有帮助。
### 陷阱
如果你的 state 变量是一个对象时，请记住，你不能只更新其中的一个字段 而不显式复制其他字段。例如，在上面的例子中，你不能写成 setPosition({ x: 100 })，因为它根本就没有 y 属性! 相反，如果你想要仅设置 x，则可执行 setPosition({ ...position, x: 100 })，或将它们分成两个 state 变量，并执行 setX(100)。
## 避免矛盾的 state
下面是带有 isSending 和 isSent 两个 state 变量的酒店反馈表单：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function FeedbackForm() {
  const [text, setText] = useState('');
  const [isSending, setIsSending] = useState(false);
  const [isSent, setIsSent] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setIsSending(true);
    await sendMessage(text);
    setIsSending(false);
    setIsSent(true);
  }

  if (isSent) {
    return <h1>Thanks for feedback!</h1>
  }

  return (
    <form onSubmit={handleSubmit}>
      <p>How was your stay at The Prancing Pony?</p>
      <textarea
        disabled={isSending}
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <br />
      <button
        disabled={isSending}
        type="submit"
      >
        Send
      </button>
      {isSending && <p>Sending...</p>}
    </form>
  );
}

// 假装发送一条消息。
function sendMessage(text) {
  return new Promise(resolve => {
    setTimeout(resolve, 2000);
  });
}
```
显示更多
尽管这段代码是有效的，但也会让一些 state “极难处理”。例如，如果你忘记同时调用 setIsSent 和 setIsSending，则可能会出现 isSending 和 isSent 同时为 true 的情况。你的组件越复杂，你就越难理解发生了什么。
因为 isSending 和 isSent 不应同时为 true，所以最好用一个 status 变量来代替它们，这个 state 变量可以采取三种有效状态其中之一：'typing' (初始), 'sending', 和 'sent':
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function FeedbackForm() {
  const [text, setText] = useState('');
  const [status, setStatus] = useState('typing');

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus('sending');
    await sendMessage(text);
    setStatus('sent');
  }

  const isSending = status === 'sending';
  const isSent = status === 'sent';

  if (isSent) {
    return <h1>Thanks for feedback!</h1>
  }

  return (
    <form onSubmit={handleSubmit}>
      <p>How was your stay at The Prancing Pony?</p>
      <textarea
        disabled={isSending}
        value={text}
        onChange={e => setText(e.target.value)}
      />
      <br />
      <button
        disabled={isSending}
        type="submit"
      >
        Send
      </button>
      {isSending && <p>Sending...</p>}
    </form>
  );
}

// 假装发送一条消息。
function sendMessage(text) {
  return new Promise(resolve => {
    setTimeout(resolve, 2000);
  });
}
```
显示更多
你仍然可以声明一些常量，以提高可读性：
```
const isSending = status === 'sending';const isSent = status === 'sent';
```
但它们不是 state 变量，所以你不必担心它们彼此失去同步。
## 避免冗余的 state
如果你能在渲染期间从组件的 props 或其现有的 state 变量中计算出一些信息，则不应该把这些信息放到该组件的 state 中。
例如，以这个表单为例。它可以运行，但你能找到其中任何冗余的 state 吗？
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [fullName, setFullName] = useState('');

  function handleFirstNameChange(e) {
    setFirstName(e.target.value);
    setFullName(e.target.value + ' ' + lastName);
  }

  function handleLastNameChange(e) {
    setLastName(e.target.value);
    setFullName(firstName + ' ' + e.target.value);
  }

  return (
    <>
      <h2>Let’s check you in</h2>
      <label>
        First name:{' '}
        <input
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:{' '}
        <input
          value={lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <p>
        Your ticket will be issued to: <b>{fullName}</b>
      </p>
    </>
  );
}
```
显示更多
这个表单有三个 state 变量：firstName、lastName 和 fullName。然而，fullName 是多余的。在渲染期间，你始终可以从 firstName 和 lastName 中计算出 fullName，因此需要把它从 state 中删除。
你可以这样做：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');

  const fullName = firstName + ' ' + lastName;

  function handleFirstNameChange(e) {
    setFirstName(e.target.value);
  }

  function handleLastNameChange(e) {
    setLastName(e.target.value);
  }

  return (
    <>
      <h2>Let’s check you in</h2>
      <label>
        First name:{' '}
        <input
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:{' '}
        <input
          value={lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <p>
        Your ticket will be issued to: <b>{fullName}</b>
      </p>
    </>
  );
}
```
显示更多
这里的 fullName 不是 一个 state 变量。相反，它是在渲染期间中计算出的：
```
const fullName = firstName + ' ' + lastName;
```
因此，更改处理程序不需要做任何特殊操作来更新它。当你调用 setFirstName 或 setLastName 时，你会触发一次重新渲染，然后下一个 fullName 将从新数据中计算出来。
深入探讨
#### 不要在 state 中镜像 props
显示更多
以下代码是体现 state 冗余的一个常见例子：
```
function Message({ messageColor }) {  const [color, setColor] = useState(messageColor);
```
这里，一个 color state 变量被初始化为 messageColor 的 prop 值。这段代码的问题在于，如果父组件稍后传递不同的 messageColor 值（例如，将其从 'blue' 更改为 'red'），则 color state 变量将不会更新！ state 仅在第一次渲染期间初始化。
这就是为什么在 state 变量中，“镜像”一些 prop 属性会导致混淆的原因。相反，你要在代码中直接使用 messageColor 属性。如果你想给它起一个更短的名称，请使用常量：
```
function Message({ messageColor }) {  const color = messageColor;
```
这种写法就不会与从父组件传递的属性失去同步。
只有当你 想要 忽略特定 props 属性的所有更新时，将 props “镜像”到 state 才有意义。按照惯例，prop 名称以 initial 或 default 开头，以阐明该 prop 的新值将被忽略：
```
function Message({ initialColor }) {  // 这个 `color` state 变量用于保存 `initialColor` 的 **初始值**。  // 对于 `initialColor` 属性的进一步更改将被忽略。  const [color, setColor] = useState(initialColor);
```
## 避免重复的 state
下面这个菜单列表组件可以让你在多种旅行小吃中选择一个：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

const initialItems = [
  { title: 'pretzels', id: 0 },
  { title: 'crispy seaweed', id: 1 },
  { title: 'granola bar', id: 2 },
];

export default function Menu() {
  const [items, setItems] = useState(initialItems);
  const [selectedItem, setSelectedItem] = useState(
    items[0]
  );

  return (
    <>
      <h2>What's your travel snack?</h2>
      <ul>
        {items.map(item => (
          <li key={item.id}>
            {item.title}
            {' '}
            <button onClick={() => {
              setSelectedItem(item);
            }}>Choose</button>
          </li>
        ))}
      </ul>
      <p>You picked {selectedItem.title}.</p>
    </>
  );
}
```
显示更多
当前，它将所选元素作为对象存储在 selectedItem state 变量中。然而，这并不好：selectedItem 的内容与 items 列表中的某个项是同一个对象。 这意味着关于该项本身的信息在两个地方产生了重复。
为什么这是个问题？让我们使每个项目都可以编辑：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

const initialItems = [
  { title: 'pretzels', id: 0 },
  { title: 'crispy seaweed', id: 1 },
  { title: 'granola bar', id: 2 },
];

export default function Menu() {
  const [items, setItems] = useState(initialItems);
  const [selectedItem, setSelectedItem] = useState(
    items[0]
  );

  function handleItemChange(id, e) {
    setItems(items.map(item => {
      if (item.id === id) {
        return {
          ...item,
          title: e.target.value,
        };
      } else {
        return item;
      }
    }));
  }

  return (
    <>
      <h2>What's your travel snack?</h2>
      <ul>
        {items.map((item, index) => (
          <li key={item.id}>
            <input
              value={item.title}
              onChange={e => {
                handleItemChange(item.id, e)
              }}
            />
            {' '}
            <button onClick={() => {
              setSelectedItem(item);
            }}>Choose</button>
          </li>
        ))}
      </ul>
      <p>You picked {selectedItem.title}.</p>
    </>
  );
}
```
显示更多
请注意，如果你首先单击菜单上的“Choose” 然后 编辑它，输入会更新，但底部的标签不会反映编辑内容。 这是因为你有重复的 state，并且你忘记更新了 selectedItem。
尽管你也可以更新 selectedItem，但更简单的解决方法是消除重复项。在下面这个例子中，你将 selectedId 保存在 state 中，而不是在 selectedItem 对象中（它创建了一个与 items 内重复的对象），然后 通过搜索 items 数组中具有该 ID 的项，以此获取 selectedItem：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

const initialItems = [
  { title: 'pretzels', id: 0 },
  { title: 'crispy seaweed', id: 1 },
  { title: 'granola bar', id: 2 },
];

export default function Menu() {
  const [items, setItems] = useState(initialItems);
  const [selectedId, setSelectedId] = useState(0);

  const selectedItem = items.find(item =>
    item.id === selectedId
  );

  function handleItemChange(id, e) {
    setItems(items.map(item => {
      if (item.id === id) {
        return {
          ...item,
          title: e.target.value,
        };
      } else {
        return item;
      }
    }));
  }

  return (
    <>
      <h2>What's your travel snack?</h2>
      <ul>
        {items.map((item, index) => (
          <li key={item.id}>
            <input
              value={item.title}
              onChange={e => {
                handleItemChange(item.id, e)
              }}
            />
            {' '}
            <button onClick={() => {
              setSelectedId(item.id);
            }}>Choose</button>
          </li>
        ))}
      </ul>
      <p>You picked {selectedItem.title}.</p>
    </>
  );
}
```
显示更多
state 过去常常是这样复制的：
- items = [{ id: 0, title: 'pretzels'}, ...]
- selectedItem = {id: 0, title: 'pretzels'}
改了之后是这样的：
- items = [{ id: 0, title: 'pretzels'}, ...]
- selectedId = 0
重复的 state 没有了，你只保留了必要的 state！
现在，如果你编辑 selected 元素，下面的消息将立即更新。这是因为 setItems 会触发重新渲染，而 items.find(...) 会找到带有更新文本的元素。你不需要在 state 中保存 选定的元素，因为只有 选定的 ID 是必要的。其余的可以在渲染期间计算。
## 避免深度嵌套的 state
想象一下，一个由行星、大陆和国家组成的旅行计划。你可能会尝试使用嵌套对象和数组来构建它的 state，就像下面这个例子：
```
App.jsplaces.jsplaces.jsReloadClearForkexport const initialTravelPlan = {
  id: 0,
  title: '(Root)',
  childPlaces: [{
    id: 1,
    title: 'Earth',
    childPlaces: [{
      id: 2,
      title: 'Africa',
      childPlaces: [{
        id: 3,
        title: 'Botswana',
        childPlaces: []
      }, {
        id: 4,
        title: 'Egypt',
        childPlaces: []
      }, {
        id: 5,
        title: 'Kenya',
        childPlaces: []
      }, {
        id: 6,
        title: 'Madagascar',
        childPlaces: []
      }, {
        id: 7,
        title: 'Morocco',
        childPlaces: []
      }, {
        id: 8,
        title: 'Nigeria',
        childPlaces: []
      }, {
        id: 9,
        title: 'South Africa',
        childPlaces: []
      }]
    }, {
      id: 10,
      title: 'Americas',
      childPlaces: [{
        id: 11,
        title: 'Argentina',
        childPlaces: []
      }, {
        id: 12,
        title: 'Brazil',
        childPlaces: []
      }, {
        id: 13,
        title: 'Barbados',
        childPlaces: []
      }, {
        id: 14,
        title: 'Canada',
        childPlaces: []
      }, {
        id: 15,
        title: 'Jamaica',
        childPlaces: []
      }, {
        id: 16,
        title: 'Mexico',
        childPlaces: []
      }, {
        id: 17,
        title: 'Trinidad and Tobago',
        childPlaces: []
      }, {
        id: 18,
        title: 'Venezuela',
        childPlaces: []
      }]
    }, {
      id: 19,
      title: 'Asia',
      childPlaces: [{
        id: 20,
        title: 'China',
        childPlaces: []
      }, {
        id: 21,
        title: 'India',
        childPlaces: []
      }, {
        id: 22,
        title: 'Singapore',
        childPlaces: []
      }, {
        id: 23,
        title: 'South Korea',
        childPlaces: []
      }, {
        id: 24,
        title: 'Thailand',
        childPlaces: []
      }, {
        id: 25,
        title: 'Vietnam',
        childPlaces: []
      }]
    }, {
      id: 26,
      title: 'Europe',
      childPlaces: [{
        id: 27,
        title: 'Croatia',
        childPlaces: [],
      }, {
        id: 28,
        title: 'France',
        childPlaces: [],
      }, {
        id: 29,
        title: 'Germany',
        childPlaces: [],
      }, {
        id: 30,
        title: 'Italy',
        childPlaces: [],
      }, {
        id: 31,
        title: 'Portugal',
        childPlaces: [],
      }, {
        id: 32,
        title: 'Spain',
        childPlaces: [],
      }, {
        id: 33,
        title: 'Turkey',
        childPlaces: [],
      }]
    }, {
      id: 34,
      title: 'Oceania',
      childPlaces: [{
        id: 35,
        title: 'Australia',
        childPlaces: [],
      }, {
        id: 36,
        title: 'Bora Bora (French Polynesia)',
        childPlaces: [],
      }, {
        id: 37,
        title: 'Easter Island (Chile)',
        childPlaces: [],
      }, {
        id: 38,
        title: 'Fiji',
        childPlaces: [],
      }, {
        id: 39,
        title: 'Hawaii (the USA)',
        childPlaces: [],
      }, {
        id: 40,
        title: 'New Zealand',
        childPlaces: [],
      }, {
        id: 41,
        title: 'Vanuatu',
        childPlaces: [],
      }]
    }]
  }, {
    id: 42,
    title: 'Moon',
    childPlaces: [{
      id: 43,
      title: 'Rheita',
      childPlaces: []
    }, {
      id: 44,
      title: 'Piccolomini',
      childPlaces: []
    }, {
      id: 45,
      title: 'Tycho',
      childPlaces: []
    }]
  }, {
    id: 46,
    title: 'Mars',
    childPlaces: [{
      id: 47,
      title: 'Corn Town',
      childPlaces: []
    }, {
      id: 48,
      title: 'Green Hill',
      childPlaces: []
    }]
  }]
};
```
显示更多
现在，假设你想添加一个按钮来删除一个你已经去过的地方。你会怎么做呢？更新嵌套的 state 需要从更改部分一直向上复制对象。删除一个深度嵌套的地点将涉及复制其整个父级地点链。这样的代码可能非常冗长。
如果 state 嵌套太深，难以轻松更新，可以考虑将其“扁平化”。 这里有一个方法可以重构上面这个数据。不同于树状结构，每个节点的 place 都是一个包含 其子节点 的数组，你可以让每个节点的 place 作为数组保存 其子节点的 ID。然后存储一个节点 ID 与相应节点的映射关系。
这个数据重组可能会让你想起看到一个数据库表：
```
App.jsplaces.jsplaces.jsReloadClearForkexport const initialTravelPlan = {
  0: {
    id: 0,
    title: '(Root)',
    childIds: [1, 42, 46],
  },
  1: {
    id: 1,
    title: 'Earth',
    childIds: [2, 10, 19, 26, 34]
  },
  2: {
    id: 2,
    title: 'Africa',
    childIds: [3, 4, 5, 6 , 7, 8, 9]
  },
  3: {
    id: 3,
    title: 'Botswana',
    childIds: []
  },
  4: {
    id: 4,
    title: 'Egypt',
    childIds: []
  },
  5: {
    id: 5,
    title: 'Kenya',
    childIds: []
  },
  6: {
    id: 6,
    title: 'Madagascar',
    childIds: []
  },
  7: {
    id: 7,
    title: 'Morocco',
    childIds: []
  },
  8: {
    id: 8,
    title: 'Nigeria',
    childIds: []
  },
  9: {
    id: 9,
    title: 'South Africa',
    childIds: []
  },
  10: {
    id: 10,
    title: 'Americas',
    childIds: [11, 12, 13, 14, 15, 16, 17, 18],
  },
  11: {
    id: 11,
    title: 'Argentina',
    childIds: []
  },
  12: {
    id: 12,
    title: 'Brazil',
    childIds: []
  },
  13: {
    id: 13,
    title: 'Barbados',
    childIds: []
  },
  14: {
    id: 14,
    title: 'Canada',
    childIds: []
  },
  15: {
    id: 15,
    title: 'Jamaica',
    childIds: []
  },
  16: {
    id: 16,
    title: 'Mexico',
    childIds: []
  },
  17: {
    id: 17,
    title: 'Trinidad and Tobago',
    childIds: []
  },
  18: {
    id: 18,
    title: 'Venezuela',
    childIds: []
  },
  19: {
    id: 19,
    title: 'Asia',
    childIds: [20, 21, 22, 23, 24, 25],
  },
  20: {
    id: 20,
    title: 'China',
    childIds: []
  },
  21: {
    id: 21,
    title: 'India',
    childIds: []
  },
  22: {
    id: 22,
    title: 'Singapore',
    childIds: []
  },
  23: {
    id: 23,
    title: 'South Korea',
    childIds: []
  },
  24: {
    id: 24,
    title: 'Thailand',
    childIds: []
  },
  25: {
    id: 25,
    title: 'Vietnam',
    childIds: []
  },
  26: {
    id: 26,
    title: 'Europe',
    childIds: [27, 28, 29, 30, 31, 32, 33],
  },
  27: {
    id: 27,
    title: 'Croatia',
    childIds: []
  },
  28: {
    id: 28,
    title: 'France',
    childIds: []
  },
  29: {
    id: 29,
    title: 'Germany',
    childIds: []
  },
  30: {
    id: 30,
    title: 'Italy',
    childIds: []
  },
  31: {
    id: 31,
    title: 'Portugal',
    childIds: []
  },
  32: {
    id: 32,
    title: 'Spain',
    childIds: []
  },
  33: {
    id: 33,
    title: 'Turkey',
    childIds: []
  },
  34: {
    id: 34,
    title: 'Oceania',
    childIds: [35, 36, 37, 38, 39, 40, 41],
  },
  35: {
    id: 35,
    title: 'Australia',
    childIds: []
  },
  36: {
    id: 36,
    title: 'Bora Bora (French Polynesia)',
    childIds: []
  },
  37: {
    id: 37,
    title: 'Easter Island (Chile)',
    childIds: []
  },
  38: {
    id: 38,
    title: 'Fiji',
    childIds: []
  },
  39: {
    id: 40,
    title: 'Hawaii (the USA)',
    childIds: []
  },
  40: {
    id: 40,
    title: 'New Zealand',
    childIds: []
  },
  41: {
    id: 41,
    title: 'Vanuatu',
    childIds: []
  },
  42: {
    id: 42,
    title: 'Moon',
    childIds: [43, 44, 45]
  },
  43: {
    id: 43,
    title: 'Rheita',
    childIds: []
  },
  44: {
    id: 44,
    title: 'Piccolomini',
    childIds: []
  },
  45: {
    id: 45,
    title: 'Tycho',
    childIds: []
  },
  46: {
    id: 46,
    title: 'Mars',
    childIds: [47, 48]
  },
  47: {
    id: 47,
    title: 'Corn Town',
    childIds: []
  },
  48: {
    id: 48,
    title: 'Green Hill',
    childIds: []
  }
};
```
显示更多
现在 state 已经“扁平化”（也称为“规范化”），更新嵌套项会变得更加容易。
现在要删除一个地点，你只需要更新两个 state 级别：
- 其 父级 地点的更新版本应该从其 childIds 数组中排除已删除的 ID。
- 其根级“表”对象的更新版本应包括父级地点的更新版本。
下面是展示如何处理它的一个示例：
```
App.jsplaces.jsApp.jsReloadClearForkimport { useState } from 'react';
import { initialTravelPlan } from './places.js';

export default function TravelPlan() {
  const [plan, setPlan] = useState(initialTravelPlan);

  function handleComplete(parentId, childId) {
    const parent = plan[parentId];
    // 创建一个其父级地点的新版本
    // 但不包括子级 ID。
    const nextParent = {
      ...parent,
      childIds: parent.childIds
        .filter(id => id !== childId)
    };
    // 更新根 state 对象...
    setPlan({
      ...plan,
      // ...以便它拥有更新的父级。
      [parentId]: nextParent
    });
  }

  const root = plan[0];
  const planetIds = root.childIds;
  return (
    <>
      <h2>Places to visit</h2>
      <ol>
        {planetIds.map(id => (
          <PlaceTree
            key={id}
            id={id}
            parentId={0}
            placesById={plan}
            onComplete={handleComplete}
          />
        ))}
      </ol>
    </>
  );
}

function PlaceTree({ id, parentId, placesById, onComplete }) {
  const place = placesById[id];
  const childIds = place.childIds;
  return (
    <li>
      {place.title}
      <button onClick={() => {
        onComplete(parentId, id);
      }}>
        Complete
      </button>
      {childIds.length > 0 &&
        <ol>
          {childIds.map(childId => (
            <PlaceTree
              key={childId}
              id={childId}
              parentId={id}
              placesById={placesById}
              onComplete={onComplete}
            />
          ))}
        </ol>
      }
    </li>
  );
}
```
显示更多
你确实可以随心所欲地嵌套 state，但是将其“扁平化”可以解决许多问题。这使得 state 更容易更新，并且有助于确保在嵌套对象的不同部分中没有重复。
深入探讨
#### 改善内存使用
显示更多
理想情况下，你还应该从“表”对象中删除已删除的项目（以及它们的子项！）以改善内存使用。还可以 使用 Immer 使更新逻辑更加简洁。
```
package.jsonApp.jsplaces.jspackage.jsonReloadClearFork{
  "dependencies": {
    "immer": "1.7.3",
    "react": "latest",
    "react-dom": "latest",
    "react-scripts": "latest",
    "use-immer": "0.5.1"
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
有时候，你也可以通过将一些嵌套 state 移动到子组件中来减少 state 的嵌套。这对于不需要保存的短暂 UI 状态非常有效，比如一个选项是否被悬停。
## 摘要
- 如果两个 state 变量总是一起更新，请考虑将它们合并为一个。
- 仔细选择你的 state 变量，以避免创建“极难处理”的 state。
- 用一种减少出错更新的机会的方式来构建你的 state。
- 避免冗余和重复的 state，这样你就不需要保持同步。
- 除非你特别想防止更新，否则不要将 props 放入 state 中。
- 对于选择类型的 UI 模式，请在 state 中保存 ID 或索引而不是对象本身。
- 如果深度嵌套 state 更新很复杂，请尝试将其展开扁平化。
## 尝试一些挑战
1. 修复一个未更新的组件 2. 修复一个损坏的打包清单 3. 修复消失的选项 4. 实现多选功能
#### 第 1 个挑战 共 4 个挑战: 修复一个未更新的组件
这个 Clock 组件接收两个属性：color 和 time。当你在选择框中选择不同的颜色时，Clock 组件将从其父组件接收到一个不同的 color 属性。然而，由于某种原因，显示的颜色没有更新。为什么？请修复这个问题。
```
Clock.jsClock.jsReloadClearForkimport { useState } from 'react';

export default function Clock(props) {
  const [color, setColor] = useState(props.color);
  return (
    <h1 style={{ color: color }}>
      {props.time}
    </h1>
  );
}
```