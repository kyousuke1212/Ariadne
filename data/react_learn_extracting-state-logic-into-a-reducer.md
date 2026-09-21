学习 React状态管理 Copy pageCopy
# 迁移状态逻辑至 Reducer 中
对于拥有许多状态更新逻辑的组件来说，过于分散的事件处理程序可能会令人不知所措。对于这种情况，你可以将组件的所有状态更新逻辑整合到一个外部函数中，这个函数叫作 reducer。
### 你将会学习到
- 什么是 reducer 函数
- 如何将 useState 重构成 useReducer
- 什么时候使用 reducer
- 如何编写一个好的 reducer
## 使用 reducer 整合状态逻辑
随着组件复杂度的增加，你将很难一眼看清所有的组件状态更新逻辑。例如，下面的 TaskApp 组件有一个数组类型的状态 tasks，并通过三个不同的事件处理程序来实现任务的添加、删除和修改：
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';

export default function TaskApp() {
  const [tasks, setTasks] = useState(initialTasks);

  function handleAddTask(text) {
    setTasks([
      ...tasks,
      {
        id: nextId++,
        text: text,
        done: false,
      },
    ]);
  }

  function handleChangeTask(task) {
    setTasks(
      tasks.map((t) => {
        if (t.id === task.id) {
          return task;
        } else {
          return t;
        }
      })
    );
  }

  function handleDeleteTask(taskId) {
    setTasks(tasks.filter((t) => t.id !== taskId));
  }

  return (
    <>
      <h1>布拉格的行程安排</h1>
      <AddTask onAddTask={handleAddTask} />
      <TaskList
        tasks={tasks}
        onChangeTask={handleChangeTask}
        onDeleteTask={handleDeleteTask}
      />
    </>
  );
}

let nextId = 3;
const initialTasks = [
  {id: 0, text: '参观卡夫卡博物馆', done: true},
  {id: 1, text: '看木偶戏', done: false},
  {id: 2, text: '打卡列侬墙', done: false},
];
```
显示更多
这个组件的每个事件处理程序都通过 setTasks 来更新状态。随着这个组件的不断迭代，其状态逻辑也会越来越多。为了降低这种复杂度，并让所有逻辑都可以存放在一个易于理解的地方，你可以将这些状态逻辑移到组件之外的一个称为 reducer 的函数中。
Reducer 是处理状态的另一种方式。你可以通过三个步骤将 useState 迁移到 useReducer：
- 将设置状态的逻辑 修改 成 dispatch 的一个 action；
- 编写 一个 reducer 函数；
- 在你的组件中 使用 reducer。
### 第 1 步: 将设置状态的逻辑修改成 dispatch 的一个 action
你的事件处理程序目前是通过设置状态来 实现逻辑的：
```
function handleAddTask(text) {  setTasks([    ...tasks,    {      id: nextId++,      text: text,      done: false,    },  ]);}function handleChangeTask(task) {  setTasks(    tasks.map((t) => {      if (t.id === task.id) {        return task;      } else {        return t;      }    })  );}function handleDeleteTask(taskId) {  setTasks(tasks.filter((t) => t.id !== taskId));}
```
移除所有的状态设置逻辑。只留下三个事件处理函数：
- handleAddTask(text) 在用户点击 “添加” 时被调用。
- handleChangeTask(task) 在用户切换任务或点击 “保存” 时被调用。
- handleDeleteTask(taskId) 在用户点击 “删除” 时被调用。
使用 reducer 管理状态与直接设置状态略有不同。它不是通过设置状态来告诉 React “要做什么”，而是通过事件处理程序 dispatch 一个 “action” 来指明 “用户刚刚做了什么”。（而状态更新逻辑则保存在其他地方！）因此，我们不再通过事件处理器直接 “设置 task”，而是 dispatch 一个 “添加/修改/删除任务” 的 action。这更加符合用户的思维。
```
function handleAddTask(text) {  dispatch({    type: 'added',    id: nextId++,    text: text,  });}function handleChangeTask(task) {  dispatch({    type: 'changed',    task: task,  });}function handleDeleteTask(taskId) {  dispatch({    type: 'deleted',    id: taskId,  });}
```
你传递给 dispatch 的对象叫做 “action”：
```
function handleDeleteTask(taskId) {  dispatch(    // "action" 对象：    {      type: 'deleted',      id: taskId,    }  );}
```
它是一个普通的 JavaScript 对象。它的结构是由你决定的，但通常来说，它应该至少包含可以表明 发生了什么事情 的信息。（在后面的步骤中，你将会学习如何添加一个 dispatch 函数。）
### 注意
action 对象可以有多种结构。
按照惯例，我们通常会添加一个字符串类型的 type 字段来描述发生了什么，并通过其它字段传递额外的信息。type 是特定于组件的，在这个例子中 added 和 addded_task 都可以。选一个能描述清楚发生的事件的名字！
```
dispatch({  // 针对特定的组件  type: 'what_happened',  // 其它字段放这里});
```
### 第 2 步: 编写一个 reducer 函数
reducer 函数就是你放置状态逻辑的地方。它接受两个参数，分别为当前 state 和 action 对象，并且返回的是更新后的 state：
```
function yourReducer(state, action) {  // 给 React 返回更新后的状态}
```
React 会将状态设置为你从 reducer 返回的状态。
在这个例子中，要将状态设置逻辑从事件处理程序移到 reducer 函数中，你需要：
- 声明当前状态（tasks）作为第一个参数；
- 声明 action 对象作为第二个参数；
- 从 reducer 返回 下一个 状态（React 会将旧的状态设置为这个最新的状态）。
下面是所有迁移到 reducer 函数的状态设置逻辑：
```
function tasksReducer(tasks, action) {  if (action.type === 'added') {    return [      ...tasks,      {        id: action.id,        text: action.text,        done: false,      },    ];  } else if (action.type === 'changed') {    return tasks.map((t) => {      if (t.id === action.task.id) {        return action.task;      } else {        return t;      }    });  } else if (action.type === 'deleted') {    return tasks.filter((t) => t.id !== action.id);  } else {    throw Error('未知 action: ' + action.type);  }}
```
由于 reducer 函数接受 state（tasks）作为参数，因此你可以 在组件之外声明它。这减少了代码的缩进级别，提升了代码的可读性。
### 注意
上面的代码使用了 if/else 语句，但是在 reducer 中使用 switch 语句 是一种惯例。两种方式结果是相同的，但 switch 语句读起来一目了然。
在本文档的后续部分我们会像这样使用：
```
function tasksReducer(tasks, action) {  switch (action.type) {    case 'added': {      return [        ...tasks,        {          id: action.id,          text: action.text,          done: false,        },      ];    }    case 'changed': {      return tasks.map((t) => {        if (t.id === action.task.id) {          return action.task;        } else {          return t;        }      });    }    case 'deleted': {      return tasks.filter((t) => t.id !== action.id);    }    default: {      throw Error('未知 action: ' + action.type);    }  }}
```
我们建议将每个 case 块包装到 { 和 } 花括号中，这样在不同 case 中声明的变量就不会互相冲突。此外，case 通常应该以 return 结尾。如果你忘了 return，代码就会 进入 到下一个 case，这就会导致错误！
如果你还不熟悉 switch 语句，使用 if/else 也是可以的。
深入探讨
#### 为什么称之为 reducer?
显示更多
尽管 reducer 可以 “减少” 组件内的代码量，但它实际上是以数组上的 reduce() 方法命名的。
reduce() 允许你将数组中的多个值 “累加” 成一个值：
```
const arr = [1, 2, 3, 4, 5];const sum = arr.reduce(  (result, number) => result + number); // 1 + 2 + 3 + 4 + 5
```
你传递给 reduce 的函数被称为 “reducer”。它接受 目前的结果 和 当前的值，然后返回 下一个结果。React 中的 reducer 和这个是一样的：它们都接受 目前的状态 和 action ，然后返回 下一个状态。这样，action 会随着时间推移累积到状态中。
你甚至可以使用 reduce() 方法以及 initialState 和 actions 数组，通过传递你的 reducer 函数来计算最终的状态：
```
index.jsindex.htmltasksReducer.jsindex.jsReloadClearForkimport tasksReducer from './tasksReducer.js';

let initialState = [];
let actions = [
  {type: 'added', id: 1, text: '参观卡夫卡博物馆'},
  {type: 'added', id: 2, text: '看木偶戏'},
  {type: 'deleted', id: 1},
  {type: 'added', id: 3, text: '打卡列侬墙'},
];

let finalState = actions.reduce(tasksReducer, initialState);

const output = document.getElementById('output');
output.textContent = JSON.stringify(finalState, null, 2);
```
你可能不需要自己做这些，但这与 React 所做的很相似！
### 第 3 步: 在组件中使用 reducer
最后，你需要将 tasksReducer 导入到组件中。记得先从 React 中导入 useReducer Hook：
```
import { useReducer } from 'react';
```
接下来，你就可以替换掉之前的 useState:
```
const [tasks, setTasks] = useState(initialTasks);
```
只需要像下面这样使用 useReducer:
```
const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);
```
useReducer 和 useState 很相似——你必须给它传递一个初始状态，它会返回一个有状态的值和一个设置该状态的函数（在这个例子中就是 dispatch 函数）。但是，它们两个之间还是有点差异的。
useReducer 钩子接受 2 个参数：
- 一个 reducer 函数
- 一个初始的 state
它返回如下内容：
- 一个有状态的值
- 一个 dispatch 函数（用来 “派发” 用户操作给 reducer）
现在一切都准备就绪了！我们在这里把 reducer 定义在了组件的末尾：
```
App.jsApp.jsReloadClearForkimport { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';

export default function TaskApp() {
  const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);

  function handleAddTask(text) {
    dispatch({
      type: 'added',
      id: nextId++,
      text: text,
    });
  }

  function handleChangeTask(task) {
    dispatch({
      type: 'changed',
      task: task,
    });
  }

  function handleDeleteTask(taskId) {
    dispatch({
      type: 'deleted',
      id: taskId,
    });
  }

  return (
    <>
      <h1>布拉格的行程安排</h1>
      <AddTask onAddTask={handleAddTask} />
      <TaskList
        tasks={tasks}
        onChangeTask={handleChangeTask}
        onDeleteTask={handleDeleteTask}
      />
    </>
  );
}

function tasksReducer(tasks, action) {
  switch (action.type) {
    case 'added': {
      return [
        ...tasks,
        {
          id: action.id,
          text: action.text,
          done: false,
        },
      ];
    }
    case 'changed': {
      return tasks.map((t) => {
        if (t.id === action.task.id) {
          return action.task;
        } else {
          return t;
        }
      });
    }
    case 'deleted': {
      return tasks.filter((t) => t.id !== action.id);
    }
    default: {
      throw Error('未知 action: ' + action.type);
    }
  }
}

let nextId = 3;
const initialTasks = [
  {id: 0, text: '参观卡夫卡博物馆', done: true},
  {id: 1, text: '看木偶戏', done: false},
  {id: 2, text: '打卡列侬墙', done: false}
];
```
显示更多
如果有需要，你甚至可以把 reducer 移到一个单独的文件中：
```
App.jstasksReducer.jsApp.jsReloadClearForkimport { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';
import tasksReducer from './tasksReducer.js';

export default function TaskApp() {
  const [tasks, dispatch] = useReducer(tasksReducer, initialTasks);

  function handleAddTask(text) {
    dispatch({
      type: 'added',
      id: nextId++,
      text: text,
    });
  }

  function handleChangeTask(task) {
    dispatch({
      type: 'changed',
      task: task,
    });
  }

  function handleDeleteTask(taskId) {
    dispatch({
      type: 'deleted',
      id: taskId,
    });
  }

  return (
    <>
      <h1>布拉格的行程安排</h1>
      <AddTask onAddTask={handleAddTask} />
      <TaskList
        tasks={tasks}
        onChangeTask={handleChangeTask}
        onDeleteTask={handleDeleteTask}
      />
    </>
  );
}

let nextId = 3;
const initialTasks = [
  {id: 0, text: '参观卡夫卡博物馆', done: true},
  {id: 1, text: '看木偶戏', done: false},
  {id: 2, text: '打卡列侬墙', done: false},
];
```
显示更多
当像这样分离关注点时，我们可以更容易地理解组件逻辑。现在，事件处理程序只通过派发 action 来指定 发生了什么，而 reducer 函数通过响应 actions 来决定 状态如何更新。
## 对比 useState 和 useReducer
Reducer 并非没有缺点！以下是比较它们的几种方法：
- 代码体积： 通常，在使用 useState 时，一开始只需要编写少量代码。而 useReducer 必须提前编写 reducer 函数和需要调度的 actions。但是，当多个事件处理程序以相似的方式修改 state 时，useReducer 可以减少代码量。
- 可读性： 当状态更新逻辑足够简单时，useState 的可读性还行。但是，一旦逻辑变得复杂起来，它们会使组件变得臃肿且难以阅读。在这种情况下，useReducer 允许你将状态更新逻辑与事件处理程序分离开来。
- 可调试性： 当使用 useState 出现问题时, 你很难发现具体原因以及为什么。 而使用 useReducer 时， 你可以在 reducer 函数中通过打印日志的方式来观察每个状态的更新，以及为什么要更新（来自哪个 action）。 如果所有 action 都没问题，你就知道问题出在了 reducer 本身的逻辑中。 然而，与使用 useState 相比，你必须单步执行更多的代码。
- 可测试性： reducer 是一个不依赖于组件的纯函数。这就意味着你可以单独对它进行测试。一般来说，我们最好是在真实环境中测试组件，但对于复杂的状态更新逻辑，针对特定的初始状态和 action，断言 reducer 返回的特定状态会很有帮助。
- 个人偏好： 并不是所有人都喜欢用 reducer，没关系，这是个人偏好问题。你可以随时在 useState 和 useReducer 之间切换，它们能做的事情是一样的！
如果你在修改某些组件状态时经常出现问题或者想给组件添加更多逻辑时，我们建议你还是使用 reducer。当然，你也不必整个项目都用 reducer，这是可以自由搭配的。你甚至可以在一个组件中同时使用 useState 和 useReducer。
## 编写一个好的 reducer
编写 reducer 时最好牢记以下两点：
- reducer 必须是纯粹的。 这一点和 状态更新函数 是相似的，reducer 是在渲染时运行的！（actions 会排队直到下一次渲染)。 这就意味着 reducer 必须纯净，即当输入相同时，输出也是相同的。它们不应该包含异步请求、定时器或者任何副作用（对组件外部有影响的操作）。它们应该以不可变值的方式去更新 对象 和 数组。
- 每个 action 都描述了一个单一的用户交互，即使它会引发数据的多个变化。 举个例子，如果用户在一个由 reducer 管理的表单（包含五个表单项）中点击了 重置按钮，那么 dispatch 一个 reset_form 的 action 比 dispatch 五个单独的 set_field 的 action 更加合理。如果你在一个 reducer 中打印了所有的 action 日志，那么这个日志应该是很清晰的，它能让你以某种步骤复现已发生的交互或响应。这对代码调试很有帮助！
## 使用 Immer 简化 reducer
与在平常的 state 中 修改对象 和 数组 一样，你可以使用 Immer 这个库来简化 reducer。在这里，useImmerReducer 让你可以通过 push 或 arr[i] = 来修改 state ：
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
Reducer 应该是纯净的，所以它们不应该去修改 state。而 Immer 为你提供了一种特殊的 draft 对象，你可以通过它安全地修改 state。在底层，Immer 会基于当前 state 创建一个副本。这就是通过 useImmerReducer 来管理 reducer 时，可以修改第一个参数，且不需要返回一个新的 state 的原因。
## 摘要
把 useState 转化为 useReducer：
- 通过事件处理函数 dispatch actions；
- 编写一个 reducer 函数，它接受传入的 state 和一个 action，并返回一个新的 state；
- 使用 useReducer 替换 useState；
- Reducer 可能需要你写更多的代码，但是这有利于代码的调试和测试。
- Reducer 必须是纯净的。
- 每个 action 都描述了一个单一的用户交互。
- 使用 Immer 来帮助你在 reducer 里直接修改状态。
## 尝试一些挑战
1. 通过事件处理函数 dispatch actions 2. 发送消息时清空输入框 3. 切换 tab 时重置输入框内容 4. 从零开始实现 useReducer
#### 第 1 个挑战 共 4 个挑战: 通过事件处理函数 dispatch actions
目前，ContactList.js 和 Chat.js 中的事件处理程序包含 // TODO 注释。这就是输入不起作用，点击按钮也不会改变收件人的原因。
将这两个 // TODO 替换为 dispatch 相应的 action。如果要查看 action 的结构和类型，请查看 messengerReducer.js 中的 reducer。reducer 已经写好了，你不需要再修改它。你只需要在 ContactList.js 和 Chat.js 中 dispatch 相应的 action 即可。
```
App.jsmessengerReducer.jsContactList.jsChat.jsApp.jsReloadClearForkimport { useReducer } from 'react';
import Chat from './Chat.js';
import ContactList from './ContactList.js';
import { initialState, messengerReducer } from './messengerReducer';

export default function Messenger() {
  const [state, dispatch] = useReducer(messengerReducer, initialState);
  const message = state.message;
  const contact = contacts.find((c) => c.id === state.selectedId);
  return (
    <div>
      <ContactList
        contacts={contacts}
        selectedId={state.selectedId}
        dispatch={dispatch}
      />
      <Chat
        key={contact.id}
        message={message}
        contact={contact}
        dispatch={dispatch}
      />
    </div>
  );
}

const contacts = [
  {id: 0, name: 'Taylor', email: 'taylor@mail.com'},
  {id: 1, name: 'Alice', email: 'alice@mail.com'},
  {id: 2, name: 'Bob', email: 'bob@mail.com'},
];
```