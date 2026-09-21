学习 React Copy pageCopy
# 状态管理
中级
随着你的应用不断变大，更有意识的去关注应用状态如何组织，以及数据如何在组件之间流动会对你很有帮助。冗余或重复的状态往往是缺陷的根源。在本节中，你将学习如何组织好状态，如何保持状态更新逻辑的可维护性，以及如何跨组件共享状态。
### 本章节
- 如何将 UI 变更视为状态变更
- 如何组织好状态
- 如何使用“状态提升”在组件之间共享状态
- 如何控制状态的保留或重置
- 如何在函数中整合复杂的状态逻辑
- 如何避免数据通过 prop 逐级透传
- 如何随着应用的增长去扩展状态管理
## 用 State 响应输入
使用 React，你不用直接从代码层面修改 UI。例如，不用编写诸如“禁用按钮”、“启用按钮”、“显示成功消息”等命令。相反，你只需要描述组件在不同状态（“初始状态”、“输入状态”、“成功状态”）下希望展现的 UI，然后根据用户输入触发状态更改。这和设计师对 UI 的理解很相似。
下面是一个使用 React 编写的反馈表单。请注意看它是如何使用 status 这个状态变量来决定启用或禁用提交按钮，以及是否显示成功消息的。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Form() {
  const [answer, setAnswer] = useState('');
  const [error, setError] = useState(null);
  const [status, setStatus] = useState('typing');

  if (status === 'success') {
    return <h1>答对了！</h1>
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setStatus('submitting');
    try {
      await submitForm(answer);
      setStatus('success');
    } catch (err) {
      setStatus('typing');
      setError(err);
    }
  }

  function handleTextareaChange(e) {
    setAnswer(e.target.value);
  }

  return (
    <>
      <h2>城市测验</h2>
      <p>
        哪个城市有把空气变成饮用水的广告牌？
      </p>
      <form onSubmit={handleSubmit}>
        <textarea
          value={answer}
          onChange={handleTextareaChange}
          disabled={status === 'submitting'}
        />
        <br />
        <button disabled={
          answer.length === 0 ||
          status === 'submitting'
        }>
          提交
        </button>
        {error !== null &&
          <p className="Error">
            {error.message}
          </p>
        }
      </form>
    </>
  );
}

function submitForm(answer) {
  // 模拟接口请求
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      let shouldError = answer.toLowerCase() !== 'lima'
      if (shouldError) {
        reject(new Error('猜的不错，但答案不对。再试试看吧！'));
      } else {
        resolve();
      }
    }, 1500);
  });
}
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 用 State 响应输入 来学习如何以状态驱动的思维处理交互。
阅读更多
## 选择 State 结构
良好的状态组织，可以区分开易于修改和调试的组件与频繁出问题的组件。最重要的原则是，状态不应包含冗余或重复的信息。如果包含一些多余的状态，我们会很容易忘记去更新它，从而导致问题产生！
例如，这个表单有一个多余的 fullName 状态变量：
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
      <h2>让我们帮你登记</h2>
      <label>
        名：{' '}
        <input
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        姓：{' '}
        <input
          value={lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <p>
        你的票据将签发给：<b>{fullName}</b>
      </p>
    </>
  );
}
```
显示更多
你可以移除它并在组件渲染时通过计算 fullName 来简化代码：
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
      <h2>让我们帮你登记</h2>
      <label>
        名：{' '}
        <input
          value={firstName}
          onChange={handleFirstNameChange}
        />
      </label>
      <label>
        姓：{' '}
        <input
          value={lastName}
          onChange={handleLastNameChange}
        />
      </label>
      <p>
        你的票将发给：<b>{fullName}</b>
      </p>
    </>
  );
}
```
显示更多
这看起来似乎只是一个小改动，但却可以避免很多潜在的问题。
## 想要仔细学习这个主题的内容吗？
阅读 选择 State 结构 来学习如何组织状态并避开错误。
阅读更多
## 在组件间共享状态
有时候你希望两个组件的状态始终同步更改。要实现这一点，可以将相关状态从这两个组件上移除，并把这些状态移到最近的父级组件，然后通过 props 将状态传递给这两个组件。这被称为“状态提升”，这是编写 React 代码时常做的事。
在以下示例中，要求每次只能激活一个面板。要实现这一点，父组件将管理激活状态并为其子组件指定 prop，而不是将激活状态保留在各自的子组件中。
```
App.jsApp.jsReloadClearForkimport { useState } from 'react';

export default function Accordion() {
  const [activeIndex, setActiveIndex] = useState(0);
  return (
    <>
      <h2>Almaty, Kazakhstan</h2>
      <Panel
        title="关于"
        isActive={activeIndex === 0}
        onShow={() => setActiveIndex(0)}
      >
        阿拉木图人口约200万，是哈萨克斯坦最大的城市。在1929年至1997年之间，它是该国首都。
      </Panel>
      <Panel
        title="词源"
        isActive={activeIndex === 1}
        onShow={() => setActiveIndex(1)}
      >
        这个名字源于哈萨克语 <span lang="kk-KZ">алма</span>，是“苹果”的意思，通常被翻译成“满是苹果”。事实上，阿拉木图周围的地区被认为是苹果的祖籍，<i lang="la">Malus sieversii</i> 被认为是目前本土苹果的祖先。
      </Panel>
    </>
  );
}

function Panel({
  title,
  children,
  isActive,
  onShow
}) {
  return (
    <section className="panel">
      <h3>{title}</h3>
      {isActive ? (
        <p>{children}</p>
      ) : (
        <button onClick={onShow}>
          显示
        </button>
      )}
    </section>
  );
}
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 在组件间共享状态 来学习如何提升状态并保持组件同步。
阅读更多
## 对 State 进行保留和重置
当你重新渲染一个组件时， React 需要决定组件树中的哪些部分要保留和更新，以及丢弃或重新创建。在大多数情况下， React 的自动处理机制已经做得足够好了。默认情况下，React 会保留树中与先前渲染的组件树“匹配”的部分。
然而，有时这并不是你想要的。例如，在下面这个程序中，输入内容后再切换收件人并不会清空输入框。这可能会导致用户不小心发错消息：
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
  { name: 'Taylor', email: 'taylor@mail.com' },
  { name: 'Alice', email: 'alice@mail.com' },
  { name: 'Bob', email: 'bob@mail.com' }
];
```
显示更多
React 允许你覆盖默认行为，可通过向组件传递一个唯一 key（如 <Chat key={email}/> 来 强制 重置其状态。这会告诉 React ，如果收件人不同，应将其作为一个 不同的 Chat 组件，需要使用新数据和 UI（比如输入框）来重新创建它。现在，在接收者之间切换时就会重置输入框——即使渲染的是同一个组件。
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
      <Chat key={to.email} contact={to} />
    </div>
  )
}

const contacts = [
  { name: 'Taylor', email: 'taylor@mail.com' },
  { name: 'Alice', email: 'alice@mail.com' },
  { name: 'Bob', email: 'bob@mail.com' }
];
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 对 State 进行保留和重置 来学习状态的生命周期以及如何控制它。
阅读更多
## 迁移状态逻辑至 Reducer 中
对于那些需要更新多个状态的组件来说，过于分散的事件处理程序可能会令人不知所措。对于这种情况，你可以在组件外部将所有状态更新逻辑合并到一个称为 “reducer” 的函数中。这样，事件处理程序就会变得简洁，因为它们只需要指定用户的 “actions”。在文件的底部，reducer 函数指定状态应该如何更新以响应每个 action！
```
App.jsApp.jsReloadClearForkimport { useReducer } from 'react';
import AddTask from './AddTask.js';
import TaskList from './TaskList.js';

export default function TaskApp() {
  const [tasks, dispatch] = useReducer(
    tasksReducer,
    initialTasks
  );

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
      task: task
    });
  }

  function handleDeleteTask(taskId) {
    dispatch({
      type: 'deleted',
      id: taskId
    });
  }

  return (
    <>
      <h1>布拉格行程</h1>
      <AddTask
        onAddTask={handleAddTask}
      />
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
      return [...tasks, {
        id: action.id,
        text: action.text,
        done: false
      }];
    }
    case 'changed': {
      return tasks.map(t => {
        if (t.id === action.task.id) {
          return action.task;
        } else {
          return t;
        }
      });
    }
    case 'deleted': {
      return tasks.filter(t => t.id !== action.id);
    }
    default: {
      throw Error('未知操作：' + action.type);
    }
  }
}

let nextId = 3;
const initialTasks = [
  { id: 0, text: '参观卡夫卡博物馆', done: true },
  { id: 1, text: '看木偶戏', done: false },
  { id: 2, text: '列侬墙图片', done: false }
];
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 迁移状态逻辑至 Reducer 中 来学习如何在 reducer 函数中整合逻辑。
阅读更多
## 使用 Context 深层传递参数
通常，你会通过 props 将信息从父组件传递给子组件。但是，如果要在组件树中深入传递一些 prop，或者树里的许多组件需要使用相同的 prop，那么传递 prop 可能会变得很麻烦。Context 允许父组件将一些信息提供给它下层的任何组件，不管该组件多深层也无需通过 props 逐层透传。
这里的 Heading 组件通过“询问”最近的 Section 来确定其标题级别。每个 Section 的级别是通过给父 Section 添加的级别来确定的。每个 Section 都向它下层的所有组件提供信息，不需要逐层传递 props，而是通过 Context 来实现。
```
App.jsSection.jsHeading.jsLevelContext.jsApp.jsReloadClearForkimport Heading from './Heading.js';
import Section from './Section.js';

export default function Page() {
  return (
    <Section>
      <Heading>大标题</Heading>
      <Section>
        <Heading>一级标题</Heading>
        <Heading>一级标题</Heading>
        <Heading>一级标题</Heading>
        <Section>
          <Heading>二级标题</Heading>
          <Heading>二级标题</Heading>
          <Heading>二级标题</Heading>
          <Section>
            <Heading>三级标题</Heading>
            <Heading>三级标题</Heading>
            <Heading>三级标题</Heading>
          </Section>
        </Section>
      </Section>
    </Section>
  );
}
```
显示更多
## 想要仔细学习这个主题的内容吗？
阅读 使用 Context 深层传递参数 来学习如何使用 Context 来代替传递 props。
阅读更多
## 使用 Reducer 和 Context 拓展你的应用
Reducer 帮助你合并组件的状态更新逻辑。Context 帮助你将信息深入传递给其他组件。你可以将 reducers 和 context 组合在一起使用，以管理复杂应用的状态。
基于这种想法，使用 reducer 来管理一个具有复杂状态的父组件。组件树中任何深度的其他组件都可以通过 context 读取其状态。还可以 dispatch 一些 action 来更新状态。
```
App.jsTasksContext.jsAddTask.jsTaskList.jsApp.jsReloadClearForkimport AddTask from './AddTask.js';
import TaskList from './TaskList.js';
import { TasksProvider } from './TasksContext.js';

export default function TaskApp() {
  return (
    <TasksProvider>
      <h1>在京都休息一天</h1>
      <AddTask />
      <TaskList />
    </TasksProvider>
  );
}
```
## 想要仔细学习这个主题的内容吗？
阅读 使用 Reducer 和 Context 拓展你的应用 来学习如何在不断增长的应用程序中扩展状态管理。
阅读更多
## 下节预告
跳转到 用 State 响应输入 这一节并开始一页页的阅读！
当然，如果你已经熟悉了这些内容，可以去读一读 脱围机制?