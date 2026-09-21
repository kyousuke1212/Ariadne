学习 React添加交互 Copy pageCopy
# 更新 state 中的对象
state 中可以保存任意类型的 JavaScript 值，包括对象。但是，你不应该直接修改存放在 React state 中的对象。相反，当你想要更新一个对象时，你需要创建一个新的对象（或者将其拷贝一份），然后将 state 更新为此对象。
### 你将会学习到
- 如何正确地更新 React state 中的对象
- 如何在不产生 mutation 的情况下更新一个嵌套对象
- 什么是不可变性（immutability），以及如何不破坏它
- 如何使用 Immer 使复制对象不那么繁琐
## 什么是 mutation？
你可以在 state 中存放任意类型的 JavaScript 值。
```
const [x, setX] = useState(0);
```
到目前为止，你已经尝试过在 state 中存放数字、字符串和布尔值，这些类型的值在 JavaScript 中是不可变（immutable）的，这意味着它们不能被改变或是只读的。你可以通过替换它们的值以触发一次重新渲染。
```
setX(5);
```
state x 从 0 变为 5，但是数字 0 本身并没有发生改变。在 JavaScript 中，无法对内置的原始值，如数字、字符串和布尔值，进行任何更改。
现在考虑 state 中存放对象的情况：
```
const [position, setPosition] = useState({ x: 0, y: 0 });
```
从技术上来讲，可以改变对象自身的内容。当你这样做时，就制造了一个 mutation：
```
position.x = 5;
```
然而，虽然严格来说 React state 中存放的对象是可变的，但你应该像处理数字、布尔值、字符串一样将它们视为不可变的。因此你应该替换它们的值，而不是对它们进行修改。
## 将 state 视为只读的
换句话说，你应该 把所有存放在 state 中的 JavaScript 对象都视为只读的。
在下面的例子中，我们用一个存放在 state 中的对象来表示指针当前的位置。当你在预览区触摸或移动光标时，红色的点本应移动。但是实际上红点仍停留在原处：
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
        position.x = e.clientX;
        position.y = e.clientY;
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
  );
}
```
显示更多
问题出在下面这段代码中。
```
onPointerMove={e => {  position.x = e.clientX;  position.y = e.clientY;}}
```
这段代码直接修改了 上一次渲染中 分配给 position 的对象。但是因为并没有使用 state 的设置函数，React 并不知道对象已更改。所以 React 没有做出任何响应。这就像在吃完饭之后才尝试去改变要点的菜一样。虽然在一些情况下，直接修改 state 可能是有效的，但我们并不推荐这么做。你应该把在渲染过程中可以访问到的 state 视为只读的。
在这种情况下，为了真正地 触发一次重新渲染，你需要创建一个新对象并把它传递给 state 的设置函数：
```
onPointerMove={e => {  setPosition({    x: e.clientX,    y: e.clientY  });}}
```
通过使用 setPosition，你在告诉 React：
- 使用这个新的对象替换 position 的值
- 然后再次渲染这个组件
现在你可以看到，当你在预览区触摸或移动光标时，红点会跟随着你的指针移动：
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
  );
}
```
显示更多
深入探讨
#### 局部 mutation 是可以接受的
显示更多
像这样的代码是有问题的，因为它改变了 state 中现有的对象：
```
position.x = e.clientX;position.y = e.clientY;
```
但是像这样的代码就 没有任何问题，因为你改变的是你刚刚创建的一个新的对象：
```
const nextPosition = {};nextPosition.x = e.clientX;nextPosition.y = e.clientY;setPosition(nextPosition);
```
事实上，它完全等同于下面这种写法：
```
setPosition({  x: e.clientX,  y: e.clientY});
```
只有当你改变已经处于 state 中的 现有 对象时，mutation 才会成为问题。而修改一个你刚刚创建的对象就不会出现任何问题，因为 还没有其他的代码引用它。改变它并不会意外地影响到依赖它的东西。这叫做“局部 mutation”。你甚至可以 在渲染的过程中 进行“局部 mutation”的操作。这种操作既便捷又没有任何问题！
## 使用展开语法复制对象
在之前的例子中，始终会根据当前指针的位置创建出一个新的 position 对象。但是通常，你会希望把 现有 数据作为你所创建的新对象的一部分。例如，你可能只想要更新表单中的一个字段，其他的字段仍然使用之前的值。
下面的代码中，输入框并不会正常运行，因为 onChange 直接修改了 state ：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [person, setPerson] = useState({
    firstName: 'Barbara',
    lastName: 'Hepworth',
    email: 'bhepworth@sculpture.com'
  });

  function handleFirstNameChange(e) {
    person.firstName = e.target.value;
  }

  function handleLastNameChange(e) {
    person.lastName = e.target.value;
  }

  function handleEmailChange(e) {
    person.email = e.target.value;
  }

  return (
    <>
      <label>
        First name:
        <input
          value={person.firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:
        <input
          value={person.lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <label>
        Email:
        <input
          value={person.email}
          onChange={handleEmailChange}
        />
      </label>
      <p>
        {person.firstName}{' '}
        {person.lastName}{' '}
        ({person.email})
      </p>
    </>
  );
}
```
显示更多
例如，下面这行代码修改了上一次渲染中的 state：
```
person.firstName = e.target.value;
```
想要实现你的需求，最可靠的办法就是创建一个新的对象并将它传递给 setPerson。但是在这里，你还需要 把当前的数据复制到新对象中，因为你只改变了其中一个字段：
```
setPerson({  firstName: e.target.value, // 从 input 中获取新的 first name  lastName: person.lastName,  email: person.email});
```
你可以使用 ... 对象展开 语法，这样你就不需要单独复制每个属性。
```
setPerson({  ...person, // 复制上一个 person 中的所有字段  firstName: e.target.value // 但是覆盖 firstName 字段});
```
现在表单可以正常运行了！
可以看到，你并没有为每个输入框单独声明一个 state。对于大型表单，将所有数据都存放在同一个对象中是非常方便的——前提是你能够正确地更新它！
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [person, setPerson] = useState({
    firstName: 'Barbara',
    lastName: 'Hepworth',
    email: 'bhepworth@sculpture.com'
  });

  function handleFirstNameChange(e) {
    setPerson({
      ...person,
      firstName: e.target.value
    });
  }

  function handleLastNameChange(e) {
    setPerson({
      ...person,
      lastName: e.target.value
    });
  }

  function handleEmailChange(e) {
    setPerson({
      ...person,
      email: e.target.value
    });
  }

  return (
    <>
      <label>
        First name:
        <input
          value={person.firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:
        <input
          value={person.lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <label>
        Email:
        <input
          value={person.email}
          onChange={handleEmailChange}
        />
      </label>
      <p>
        {person.firstName}{' '}
        {person.lastName}{' '}
        ({person.email})
      </p>
    </>
  );
}
```
显示更多
请注意 ... 展开语法本质是是“浅拷贝”——它只会复制一层。这使得它的执行速度很快，但是也意味着当你想要更新一个嵌套属性时，你必须得多次使用展开语法。
深入探讨
#### 使用一个事件处理函数来更新多个字段
显示更多
你也可以在对象的定义中使用 [ 和 ] 括号来实现属性的动态命名。下面是同一个例子，但它使用了一个事件处理函数而不是三个：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [person, setPerson] = useState({
    firstName: 'Barbara',
    lastName: 'Hepworth',
    email: 'bhepworth@sculpture.com'
  });

  function handleChange(e) {
    setPerson({
      ...person,
      [e.target.name]: e.target.value
    });
  }

  return (
    <>
      <label>
        First name:
        <input
          name="firstName"
          value={person.firstName}
          onChange={handleChange}
        />
      </label>
      <label>
        Last name:
        <input
          name="lastName"
          value={person.lastName}
          onChange={handleChange}
        />
      </label>
      <label>
        Email:
        <input
          name="email"
          value={person.email}
          onChange={handleChange}
        />
      </label>
      <p>
        {person.firstName}{' '}
        {person.lastName}{' '}
        ({person.email})
      </p>
    </>
  );
}
```
显示更多
在这里，e.target.name 引用了 <input> 这个 DOM 元素的 name 属性。
## 更新一个嵌套对象
考虑下面这种结构的嵌套对象：
```
const [person, setPerson] = useState({  name: 'Niki de Saint Phalle',  artwork: {    title: 'Blue Nana',    city: 'Hamburg',    image: 'https://react.dev/images/docs/scientists/Sd1AgUOm.jpg',  }});
```
如果你想要更新 person.artwork.city 的值，用 mutation 来实现的方法非常容易理解：
```
person.artwork.city = 'New Delhi';
```
但是在 React 中，你需要将 state 视为不可变的！为了修改 city 的值，你首先需要创建一个新的 artwork 对象（其中预先填充了上一个 artwork 对象中的数据），然后创建一个新的 person 对象，并使得其中的 artwork 属性指向新创建的 artwork 对象：
```
const nextArtwork = { ...person.artwork, city: 'New Delhi' };const nextPerson = { ...person, artwork: nextArtwork };setPerson(nextPerson);
```
或者，写成一个函数调用：
```
setPerson({  ...person, // 复制其它字段的数据  artwork: { // 替换 artwork 字段    ...person.artwork, // 复制之前 person.artwork 中的数据    city: 'New Delhi' // 但是将 city 的值替换为 New Delhi！  }});
```
这虽然看起来有点冗长，但对于很多情况都能有效地解决问题：
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
深入探讨
#### 对象并非是真正嵌套的
显示更多
下面这个对象从代码上来看是“嵌套”的：
```
let obj = {  name: 'Niki de Saint Phalle',  artwork: {    title: 'Blue Nana',    city: 'Hamburg',    image: 'https://react.dev/images/docs/scientists/Sd1AgUOm.jpg',  }};
```
然而，当我们思考对象的特性时，“嵌套”并不是一个非常准确的方式。当这段代码运行的时候，不存在“嵌套”的对象。你实际上看到的是两个不同的对象：
```
let obj1 = {  title: 'Blue Nana',  city: 'Hamburg',  image: 'https://react.dev/images/docs/scientists/Sd1AgUOm.jpg',};let obj2 = {  name: 'Niki de Saint Phalle',  artwork: obj1};
```
对象 obj1 并不处于 obj2 的“内部”。例如，下面的代码中，obj3 中的属性也可以指向 obj1：
```
let obj1 = {  title: 'Blue Nana',  city: 'Hamburg',  image: 'https://react.dev/images/docs/scientists/Sd1AgUOm.jpg',};let obj2 = {  name: 'Niki de Saint Phalle',  artwork: obj1};let obj3 = {  name: 'Copycat',  artwork: obj1};
```
如果你直接修改 obj3.artwork.city，就会同时影响 obj2.artwork.city 和 obj1.city。这是因为 obj3.artwork、obj2.artwork 和 obj1 都指向同一个对象。当你用“嵌套”的方式看待对象时，很难看出这一点。相反，它们是相互独立的对象，只不过是用属性“指向”彼此而已。
### 使用 Immer 编写简洁的更新逻辑
如果你的 state 有多层的嵌套，你或许应该考虑 将其扁平化。但是，如果你不想改变 state 的数据结构，你可能更喜欢用一种更便捷的方式来实现嵌套展开的效果。Immer 是一个非常流行的库，它可以让你使用简便但可以直接修改的语法编写代码，并会帮你处理好复制的过程。通过使用 Immer，你写出的代码看起来就像是你“打破了规则”而直接修改了对象：
```
updatePerson(draft => {  draft.artwork.city = 'Lagos';});
```
但是不同于一般的 mutation，它并不会覆盖之前的 state！
深入探讨
#### Immer 是如何运行的？
显示更多
由 Immer 提供的 draft 是一种特殊类型的对象，被称为 Proxy，它会记录你用它所进行的操作。这就是你能够随心所欲地直接修改对象的原因所在！从原理上说，Immer 会弄清楚 draft 对象的哪些部分被改变了，并会依照你的修改创建出一个全新的对象。
尝试使用 Immer:
- 运行 npm install use-immer 添加 Immer 依赖
- 用 import { useImmer } from 'use-immer' 替换掉 import { useState } from 'react'
下面我们把上面的例子用 Immer 实现一下：
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
可以看到，事件处理函数变得更简洁了。你可以随意在一个组件中同时使用 useState 和 useImmer。如果你想要写出更简洁的更新处理函数，Immer 会是一个不错的选择，尤其是当你的 state 中有嵌套，并且复制对象会带来重复的代码时。
深入探讨
#### 为什么在 React 中不推荐直接修改 state？
显示更多
有以下几个原因：
- 调试：如果你使用 console.log 并且不直接修改 state，你之前日志中的 state 的值就不会被新的 state 变化所影响。这样你就可以清楚地看到两次渲染之间 state 的值发生了什么变化
- 优化：React 常见的 优化策略 依赖于如果之前的 props 或者 state 的值和下一次相同就跳过渲染。如果你从未直接修改 state ，那么你就可以很快看到 state 是否发生了变化。如果 prevObj === obj，那么你就可以肯定这个对象内部并没有发生改变。
- 新功能：我们正在构建的 React 的新功能依赖于 state 被 像快照一样看待 的理念。如果你直接修改 state 的历史版本，可能会影响你使用这些新功能。
- 需求变更：有些应用功能在不出现任何修改的情况下会更容易实现，比如实现撤销/恢复、展示修改历史，或是允许用户把表单重置成某个之前的值。这是因为你可以把 state 之前的拷贝保存到内存中，并适时对其进行再次使用。如果一开始就用了直接修改 state 的方式，那么后面要实现这样的功能就会变得非常困难。
- 更简单的实现：React 并不依赖于 mutation ，所以你不需要对对象进行任何特殊操作。它不需要像很多“响应式”的解决方案一样去劫持对象的属性、总是用代理把对象包裹起来，或者在初始化时做其他工作。这也是 React 允许你把任何对象存放在 state 中——不管对象有多大——而不会造成有任何额外的性能或正确性问题的原因。
在实践中，你经常可以“侥幸”直接修改 state 而不出现什么问题，但是我们强烈建议你不要这样做，这样你就可以使用我们秉承着这种理念开发的 React 新功能。未来的贡献者甚至是你未来的自己都会感谢你的！
## 摘要
- 将 React 中所有的 state 都视为不可直接修改的。
- 当你在 state 中存放对象时，直接修改对象并不会触发重渲染，并会改变前一次渲染“快照”中 state 的值。
- 不要直接修改一个对象，而要为它创建一个 新 版本，并通过把 state 设置成这个新版本来触发重新渲染。
- 你可以使用这样的 {...obj, something: 'newValue'} 对象展开语法来创建对象的拷贝。
- 对象的展开语法是浅层的：它的复制深度只有一层。
- 想要更新嵌套对象，你需要从你更新的位置开始自底向上为每一层都创建新的拷贝。
- 想要减少重复的拷贝代码，可以使用 Immer。
## 尝试一些挑战
1. 修复错误的 state 更新代码 2. 发现并修复 mutation 3. 使用 Immer 更新对象
#### 第 1 个挑战 共 3 个挑战: 修复错误的 state 更新代码
这个表单有几个 bug。试着点击几次增加分数的按钮。你会注意到分数并没有增加。然后试着编辑一下名字字段，你会注意到分数突然“响应”了你之前的修改。最后，试着编辑一下姓氏字段，你会发现分数完全消失了。
你的任务就是修复所有的这些 bug。在你修复它们的同时，解释一下它们为什么会产生。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Scoreboard() {
  const [player, setPlayer] = useState({
    firstName: 'Ranjani',
    lastName: 'Shettar',
    score: 10,
  });

  function handlePlusClick() {
    player.score++;
  }

  function handleFirstNameChange(e) {
    setPlayer({
      ...player,
      firstName: e.target.value,
    });
  }

  function handleLastNameChange(e) {
    setPlayer({
      lastName: e.target.value
    });
  }

  return (
    <>
      <label>
        Score: <b>{player.score}</b>
        {' '}
        <button onClick={handlePlusClick}>
          +1
        </button>
      </label>
      <label>
        First name:
        <input
          value={player.firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        Last name:
        <input
          value={player.lastName}
          onChange={handleLastNameChange}
        />
      </label>
    </>
  );
}
```