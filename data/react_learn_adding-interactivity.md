学习 React Copy pageCopy
# 添加交互
界面上的控件会根据用户的输入而更新。例如，点击按钮切换轮播图的展示。在 React 中，随时间变化的数据被称为状态（state）。你可以向任何组件添加状态，并按需进行更新。在本章节中，你将学习如何编写处理交互的组件，更新它们的状态，并根据时间变化显示不同的效果。
### 本章节
- 如何处理用户发起的事件
- 如何用状态使组件“记住”信息
- React 是如何分两个阶段更新 UI 的
- 为什么状态在你改变后没有立即更新
- 如何排队进行多个状态的更新
- 如何更新状态中的对象
- 如何更新状态中的数组
## 响应事件
React 允许你向 JSX 中添加事件处理程序。事件处理程序是你自己的函数，它将在用户交互时被触发，如点击、悬停、焦点在表单输入框上等等。
<button> 等内置组件只支持内置浏览器事件，如 onClick。但是，你也可以创建你自己的组件，并给它们的事件处理程序 props 指定你喜欢的任何特定于应用的名称。
```
App.jsApp.jsReloadClearForkexport default function App() {
  return (
    <Toolbar
      onPlayMovie={() => alert('Playing!')}
      onUploadImage={() => alert('Uploading!')}
    />
  );
}

function Toolbar({ onPlayMovie, onUploadImage }) {
  return (
    <div>
      <Button onClick={onPlayMovie}>
        Play Movie
      </Button>
      <Button onClick={onUploadImage}>
        Upload Image
      </Button>
    </div>
  );
}

function Button({ onClick, children }) {
  return (
    <button onClick={onClick}>
      {children}
    </button>
  );
}
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 响应事件 了解如何添加事件处理程序。
阅读更多
## State: 组件的记忆
组件通常需要根据交互改变屏幕上的内容。在表单中键入更新输入栏，在轮播图上点击“下一个”改变显示的图片，点击“购买”将产品放入购物车。组件需要“记住”一些东西：当前的输入值、当前的图片、购物车。在 React 中，这种特定于组件的记忆被称为状态。
你可以用 useState Hook 为组件添加状态。Hook 是能让你的组件使用 React 功能的特殊函数（状态是这些功能之一）。useState Hook 让你声明一个状态变量。它接收初始状态并返回一对值：当前状态，以及一个让你更新状态的设置函数。
```
const [index, setIndex] = useState(0);const [showMore, setShowMore] = useState(false);
```
下面是一个图库，演示如何使用并在点击时更新状态：
```
App.jsdata.jsApp.jsReloadClearForkimport { useState } from 'react';
import { sculptureList } from './data.js';

export default function Gallery() {
  const [index, setIndex] = useState(0);
  const [showMore, setShowMore] = useState(false);
  const hasNext = index < sculptureList.length - 1;

  function handleNextClick() {
    if (hasNext) {
      setIndex(index + 1);
    } else {
      setIndex(0);
    }
  }

  function handleMoreClick() {
    setShowMore(!showMore);
  }

  let sculpture = sculptureList[index];
  return (
    <>
      <button onClick={handleNextClick}>
        Next
      </button>
      <h2>
        <i>{sculpture.name} </i>
        by {sculpture.artist}
      </h2>
      <h3>
        ({index + 1} of {sculptureList.length})
      </h3>
      <button onClick={handleMoreClick}>
        {showMore ? 'Hide' : 'Show'} details
      </button>
      {showMore && <p>{sculpture.description}</p>}
      <img
        src={sculpture.url}
        alt={sculpture.alt}
      />
    </>
  );
}
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 State: 组件的记忆 了解如何记住一个值并在交互时更新它。
阅读更多
## 渲染和提交
在你的组件显示在屏幕上之前，它们必须由 React 进行渲染。理解这个过程中的步骤有助于你思考你的代码如何执行并解释其行为。
想象一下，你的组件是厨房里的厨师，用食材制作出美味的菜肴。在这个场景中，React 是服务员，负责提出顾客的要求，并给顾客上菜。这个请求和服务 UI 的过程有三个步骤：
- 触发渲染（将食客的订单送到厨房）
- 渲染组件（在厨房准备订单）
- 提交到 DOM（将订单送到桌前）
- Trigger
- Render
- Commit
Rachel Lee Nabors 绘图
## 想要仔细学习这个主题的内容吗？
阅读 渲染和提交 了解 UI 更新的生命周期。
阅读更多
## state 如同一张快照
与普通 JavaScript 变量不同，React 状态的行为更像一个快照。设置它并不改变你已有的状态变量，而是触发一次重新渲染。这在一开始可能会让人感到惊讶！
```
console.log(count);  // 0setCount(count + 1); // 请求用 1 重新渲染console.log(count);  // 仍然是 0！
```
React 这样工作是为了帮助你避免微妙的 bug。这里有一个小的聊天应用程序。试着猜一猜，如果先按下“发送”，然后再把收件人改为 Bob，会发生什么？五秒钟后，谁的名字会出现在 alert 中？
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [to, setTo] = useState('Alice');
  const [message, setMessage] = useState('Hello');

  function handleSubmit(e) {
    e.preventDefault();
    setTimeout(() => {
      alert(`You said ${message} to ${to}`);
    }, 5000);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        To:{' '}
        <select
          value={to}
          onChange={e => setTo(e.target.value)}>
          <option value="Alice">Alice</option>
          <option value="Bob">Bob</option>
        </select>
      </label>
      <textarea
        placeholder="Message"
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <button type="submit">Send</button>
    </form>
  );
}
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 state 如同一张快照 了解为什么状态在事件处理程序中是“固定的”和不变的。
阅读更多
## 把一系列 state 更新加入队列
这个组件有问题：点击“+3”只能增加一次分数。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Counter() {
  const [score, setScore] = useState(0);

  function increment() {
    setScore(score + 1);
  }

  return (
    <>
      <button onClick={() => increment()}>+1</button>
      <button onClick={() => {
        increment();
        increment();
        increment();
      }}>+3</button>
      <h1>Score: {score}</h1>
    </>
  )
}
```
显示更多
state 如同一张快照 解释了为什么会出现这种情况。设置状态会请求一个新的重新渲染，但不会在已运行的代码中更改它。所以在你调用 setScore(score + 1) 后，score 仍然是 0。
```
console.log(score);  // 0setScore(score + 1); // setScore(0 + 1);console.log(score);  // 0setScore(score + 1); // setScore(0 + 1);console.log(score);  // 0setScore(score + 1); // setScore(0 + 1);console.log(score);  // 0
```
你可以通过在设置状态时传递一个 更新器函数 来解决这个问题。注意用 setScore(s => s + 1) 替换 setScore(score + 1) 是如何修复“+3”按钮的。如果你需要排队进行多次状态更新，那么这非常方便。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Counter() {
  const [score, setScore] = useState(0);

  function increment() {
    setScore(s => s + 1);
  }

  return (
    <>
      <button onClick={() => increment()}>+1</button>
      <button onClick={() => {
        increment();
        increment();
        increment();
      }}>+3</button>
      <h1>Score: {score}</h1>
    </>
  )
}
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 把一系列 state 更新加入队列 了解如何在下一次渲染前排队多个更新。
阅读更多
## 更新 state 中的对象
状态可以持有任何类型的 JavaScript 值，包括对象。但你不应该直接改变你在 React 状态中持有的对象和数组。相反，当你想更新一个对象和数组时，你需要创建一个新的对象（或复制现有的对象），然后用这个副本来更新状态。
通常情况下，你会使用 ... 展开语法来复制你想改变的对象和数组。例如，更新一个嵌套对象可以是这样的：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [person, setPerson] = useState({
    name: 'Niki de Saint Phalle',
    artwork: {
      title: 'Blue Nana',
      city: 'Hamburg',
      image: 'https://react.dev/images/docs/scientists/Sd1AgUOm.jpg',
    }
  });

  function handleNameChange(e) {
    setPerson({
      ...person,
      name: e.target.value
    });
  }

  function handleTitleChange(e) {
    setPerson({
      ...person,
      artwork: {
        ...person.artwork,
        title: e.target.value
      }
    });
  }

  function handleCityChange(e) {
    setPerson({
      ...person,
      artwork: {
        ...person.artwork,
        city: e.target.value
      }
    });
  }

  function handleImageChange(e) {
    setPerson({
      ...person,
      artwork: {
        ...person.artwork,
        image: e.target.value
      }
    });
  }

  return (
    <>
      <label>
        Name:
        <input
          value={person.name}
          onChange={handleNameChange}
        />
      </label>
      <label>
        Title:
        <input
          value={person.artwork.title}
          onChange={handleTitleChange}
        />
      </label>
      <label>
        City:
        <input
          value={person.artwork.city}
          onChange={handleCityChange}
        />
      </label>
      <label>
        Image:
        <input
          value={person.artwork.image}
          onChange={handleImageChange}
        />
      </label>
      <p>
        <i>{person.artwork.title}</i>
        {' by '}
        {person.name}
        <br />
        (located in {person.artwork.city})
      </p>
      <img
        src={person.artwork.image}
        alt={person.artwork.title}
      />
    </>
  );
}
```
显示更多
如果在代码中复制对象感觉乏味，可以使用 Immer 之类的库来减少重复代码：
```
package.jsonApp.jspackage.jsonReloadClearFork{
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
## 想要仔细学习这个主题的内容吗？
阅读 更新 state 中的对象 了解如何正确地更新对象。
阅读更多
## 更新 state 中的数组
数组是另一种可以存在状态中的可变 JavaScript 对象，应将其视为只读。就像对象一样，当你想更新存在状态中的数组时，你需要创建一个新数组（或者复制现有数组），然后用新数组来更新状态。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

const initialList = [
  { id: 0, title: 'Big Bellies', seen: false },
  { id: 1, title: 'Lunar Landscape', seen: false },
  { id: 2, title: 'Terracotta Army', seen: true },
];

export default function BucketList() {
  const [list, setList] = useState(
    initialList
  );

  function handleToggle(artworkId, nextSeen) {
    setList(list.map(artwork => {
      if (artwork.id === artworkId) {
        return { ...artwork, seen: nextSeen };
      } else {
        return artwork;
      }
    }));
  }

  return (
    <>
      <h1>Art Bucket List</h1>
      <h2>My list of art to see:</h2>
      <ItemList
        artworks={list}
        onToggle={handleToggle} />
    </>
  );
}

function ItemList({ artworks, onToggle }) {
  return (
    <ul>
      {artworks.map(artwork => (
        <li key={artwork.id}>
          <label>
            <input
              type="checkbox"
              checked={artwork.seen}
              onChange={e => {
                onToggle(
                  artwork.id,
                  e.target.checked
                );
              }}
            />
            {artwork.title}
          </label>
        </li>
      ))}
    </ul>
  );
}
```
显示更多
如果在代码中复制数组感觉乏味，可以使用 Immer 之类的库来减少重复代码：
```
package.jsonApp.jspackage.jsonReloadClearFork{
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
## 想要仔细学习这个主题的内容吗？
阅读 更新 state 中的数组 了解如何正确地更新数组。
阅读更多
## 下节预告
前往 响应事件 开始逐页阅读本章！
或者，如果你已经熟悉这些主题，不妨看看 状态管理