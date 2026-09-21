API 参考Hook Copy pageCopy
# useContext
useContext 是一个 React Hook，可以让你读取和订阅组件中的 context。
```
const value = useContext(SomeContext)
```
参考
- useContext(SomeContext)
用法
- 向组件树深层传递数据
- 通过 context 更新传递的数据
- 指定后备方案默认值
- 覆盖组件树一部分的 context
- 在传递对象和函数时优化重新渲染
疑难解答
- 我的组件获取不到 provider 传递的值
- 尽管设置了不一样的默认值，但是我总是从 context 中得到 undefined
## 参考
### useContext(SomeContext)
在组件的顶层调用 useContext 来读取和订阅 context。
```
import { useContext } from 'react';function MyComponent() {  const theme = useContext(ThemeContext);  // ...
```
请看下方更多示例。
#### 参数
- SomeContext：先前用 createContext 创建的 context。context 本身不包含信息，它只代表你可以提供或从组件中读取的信息类型。
#### 返回值
useContext 为调用组件返回 context 的值。它被确定为传递给树中调用组件上方最近的 SomeContext 的 value。如果没有这样的 provider，那么返回值将会是为创建该 context 传递给 createContext 的 defaultValue。返回的值始终是最新的。如果 context 发生变化，React 会自动重新渲染读取 context 的组件。
#### 注意事项
- 组件中的 useContext() 调用不受 同一 组件返回的 provider 的影响。相应的 <Context> 需要位于调用 useContext() 的组件 之上。
- 从 provider 接收到不同的 value 开始，React 自动重新渲染使用了该特定 context 的所有子级。先前的值和新的值会使用 Object.is 来做比较。使用 memo 来跳过重新渲染并不妨碍子级接收到新的 context 值。
- 如果你的构建系统在输出中产生重复的模块（可能发生在符号链接中），这可能会破坏 context。通过 context 传递数据只有在用于传递 context 的 SomeContext 和用于读取数据的  SomeContext 是完全相同的对象时才有效，这是由 === 比较决定的。
## 用法
### 向组件树深层传递数据
在组件的最顶级调用 useContext 来读取和订阅 context。
```
import { useContext } from 'react';function Button() {  const theme = useContext(ThemeContext);  // ...
```
useContext 返回你向 context 传递的 context value。为了确定 context 值，React 搜索组件树，为这个特定的 context 向上查找最近的 context provider。
若要将 context 传递给 Button，请将其或其父组件之一包装到相应的 context provider：
```
function MyPage() {  return (    <ThemeContext value="dark">      <Form />    </ThemeContext>  );}function Form() {  // ... 在内部渲染 buttons ...}
```
provider 和 Button 之间有多少层组件并不重要。当 Form 中的任何位置的 Button 调用 useContext(ThemeContext) 时，它都将接收 "dark" 作为值。
### 陷阱
useContext() 总是在调用它的组件 上面 寻找最近的 provider。它向上搜索， 不考虑 调用 useContext() 的组件中的 provider。
```
App.jsApp.jsReloadClearForkimport { createContext, useContext } from 'react';

const ThemeContext = createContext(null);

export default function MyApp() {
  return (
    <ThemeContext value="dark">
      <Form />
    </ThemeContext>
  )
}

function Form() {
  return (
    <Panel title="Welcome">
      <Button>Sign up</Button>
      <Button>Log in</Button>
    </Panel>
  );
}

function Panel({ title, children }) {
  const theme = useContext(ThemeContext);
  const className = 'panel-' + theme;
  return (
    <section className={className}>
      <h1>{title}</h1>
      {children}
    </section>
  )
}

function Button({ children }) {
  const theme = useContext(ThemeContext);
  const className = 'button-' + theme;
  return (
    <button className={className}>
      {children}
    </button>
  );
}
```
显示更多
### 通过 context 更新传递的数据
通常，你会希望 context 随着时间的推移而改变。要更新 context，请将其与 state 结合。在父组件中声明一个状态变量，并将当前状态作为 context value 传递给 provider。
```
function MyPage() {  const [theme, setTheme] = useState('dark');  return (    <ThemeContext value={theme}>      <Form />      <Button onClick={() => {        setTheme('light');      }}>       Switch to light theme      </Button>    </ThemeContext>  );}
```
现在 provider 中的任何一个 Button 都会接收到当前的 theme 值。如果调用 setTheme 来更新传递给 provider 的 theme 值，则所有 Button 组件都将使用新的值 'light' 来重新渲染。
#### 更新 context 的例子
1. 通过 context 来更新数据 2. 通过 context 更新对象 3. 同时使用多个 context 4. 把 provider 抽离成组件 5. 使用 context 和 reducer 进行扩展
#### 第 1 个示例 共 5 个示例: 通过 context 来更新数据
在这个示例中，MyApp 组件包含一个状态变量，然后该变量被传递给 ThemeContext provider。选中“Dark mode”复选框更新状态。更改提供的值将重新渲染使用该 context 的所有组件。
```
App.jsApp.jsReloadClearForkimport { createContext, useContext, useState } from 'react';

const ThemeContext = createContext(null);

export default function MyApp() {
  const [theme, setTheme] = useState('light');
  return (
    <ThemeContext value={theme}>
      <Form />
      <label>
        <input
          type="checkbox"
          checked={theme === 'dark'}
          onChange={(e) => {
            setTheme(e.target.checked ? 'dark' : 'light')
          }}
        />
        Use dark mode
      </label>
    </ThemeContext>
  )
}

function Form({ children }) {
  return (
    <Panel title="Welcome">
      <Button>Sign up</Button>
      <Button>Log in</Button>
    </Panel>
  );
}

function Panel({ title, children }) {
  const theme = useContext(ThemeContext);
  const className = 'panel-' + theme;
  return (
    <section className={className}>
      <h1>{title}</h1>
      {children}
    </section>
  )
}

function Button({ children }) {
  const theme = useContext(ThemeContext);
  const className = 'button-' + theme;
  return (
    <button className={className}>
      {children}
    </button>
  );
}
```
显示更多
注意，value="dark" 传递 "dark" 字符串，但 value={theme} 传递带有 JSX 花括号 的 JavaScript theme 变量的值。花括号还允许传递非字符串的 context 值。
下一个示例
### 指定后备方案默认值
如果 React 没有在父树中找到该特定 context 的任何 provider，useContext() 返回的 context 值将等于你在 创建 context 时指定的 默认值：
```
const ThemeContext = createContext(null);
```
默认值 从不改变。如果你想要更新 context，请按 上述方式 将其与状态一起使用。
通常，除了 null，还有一些更有意义的值可以用作默认值，例如：
```
const ThemeContext = createContext('light');
```
这样，如果你不小心渲染了没有相应 provider 的某个组件，它也不会出错。这也有助于你的组件在测试环境中很好地运行，而无需在测试中设置许多 provider。
在下面的例子中，“Toggle theme”按钮总是处于 light 状态，因为它位于 任何主题的 context provider 之外，且 context 主题的默认值是 'light'。试着编辑默认主题为 'dark'。
```
App.jsApp.jsReloadClearForkimport { createContext, useContext, useState } from 'react';

const ThemeContext = createContext('light');

export default function MyApp() {
  const [theme, setTheme] = useState('light');
  return (
    <>
      <ThemeContext value={theme}>
        <Form />
      </ThemeContext>
      <Button onClick={() => {
        setTheme(theme === 'dark' ? 'light' : 'dark');
      }}>
        Toggle theme
      </Button>
    </>
  )
}

function Form({ children }) {
  return (
    <Panel title="Welcome">
      <Button>Sign up</Button>
      <Button>Log in</Button>
    </Panel>
  );
}

function Panel({ title, children }) {
  const theme = useContext(ThemeContext);
  const className = 'panel-' + theme;
  return (
    <section className={className}>
      <h1>{title}</h1>
      {children}
    </section>
  )
}

function Button({ children, onClick }) {
  const theme = useContext(ThemeContext);
  const className = 'button-' + theme;
  return (
    <button className={className} onClick={onClick}>
      {children}
    </button>
  );
}
```
显示更多
### 覆盖组件树一部分的 context
通过在 provider 中使用不同的值包装树的某个部分，可以覆盖该部分的 context。
```
<ThemeContext value="dark">  ...  <ThemeContext value="light">    <Footer />  </ThemeContext>  ...</ThemeContext>
```
你可以根据需要多次嵌套和覆盖 provider。
#### Examples of overriding context
1. 覆盖主题 2. 自动嵌套标题
#### 第 1 个示例 共 2 个示例: 覆盖主题
这里，与 Footer 外的值为（"dark"）的按钮相比，里面 的按钮接收到一个不一样的 context 值（"light"）。
```
App.jsApp.jsReloadClearForkimport { createContext, useContext } from 'react';

const ThemeContext = createContext(null);

export default function MyApp() {
  return (
    <ThemeContext value="dark">
      <Form />
    </ThemeContext>
  )
}

function Form() {
  return (
    <Panel title="Welcome">
      <Button>Sign up</Button>
      <Button>Log in</Button>
      <ThemeContext value="light">
        <Footer />
      </ThemeContext>
    </Panel>
  );
}

function Footer() {
  return (
    <footer>
      <Button>Settings</Button>
    </footer>
  );
}

function Panel({ title, children }) {
  const theme = useContext(ThemeContext);
  const className = 'panel-' + theme;
  return (
    <section className={className}>
      {title && <h1>{title}</h1>}
      {children}
    </section>
  )
}

function Button({ children }) {
  const theme = useContext(ThemeContext);
  const className = 'button-' + theme;
  return (
    <button className={className}>
      {children}
    </button>
  );
}
```
显示更多下一个示例
### 在传递对象和函数时优化重新渲染
你可以通过 context 传递任何值，包括对象和函数。
```
function MyApp() {  const [currentUser, setCurrentUser] = useState(null);  function login(response) {    storeCredentials(response.credentials);    setCurrentUser(response.user);  }  return (    <AuthContext value={{ currentUser, login }}>      <Page />    </AuthContext>  );}
```
此处，context value 是一个具有两个属性的 JavaScript 对象，其中一个是函数。每当 MyApp 出现重新渲染（例如，路由更新）时，这里将会是一个 不同的 对象指向 不同的 函数，因此 React 还必须重新渲染树中调用 useContext(AuthContext) 的所有组件。
在较小的应用程序中，这不是问题。但是，如果基础数据如 currentUser 没有更改，则不需要重新渲染它们。为了帮助 React 利用这一点，你可以使用 useCallback 包装 login 函数，并将对象创建包装到 useMemo 中。这是一个性能优化的例子：
```
import { useCallback, useMemo } from 'react';function MyApp() {  const [currentUser, setCurrentUser] = useState(null);  const login = useCallback((response) => {    storeCredentials(response.credentials);    setCurrentUser(response.user);  }, []);  const contextValue = useMemo(() => ({    currentUser,    login  }), [currentUser, login]);  return (    <AuthContext value={contextValue}>      <Page />    </AuthContext>  );}
```
根据以上改变，即使 MyApp 需要重新渲染，调用 useContext(AuthContext) 的组件也不需要重新渲染，除非 currentUser 发生了变化。
阅读更多关于 useMemo 和 useCallback 的内容。
## 疑难解答
### 我的组件获取不到 provider 传递的值
这里有几种常见的情况会引起这个问题：
- 你在调用 useContext() 的同一组件（或下层）渲染 <SomeContext>。把 <SomeContext> 向调用 useContext() 组件 之上和之外 移动。
- 你可能忘记了使用 <SomeContext> 包装组件，或者你可能将组件放在树的不同部分。使用 React DevTools 检查组件树的层级是否正确。
- 你的工具可能会遇到一些构建问题，导致你在传值组件中的所看到的 SomeContext 和读值组件中所看到的 SomeContext 是两个不同的对象。例如，如果使用符号链接，就会发生这种情况。你可以通过将它们赋值给全局对象如 window.SomeContext1 和 window.SomeContext2 来验证这种情况。然后在控制台检查 window.SomeContext1 === window.SomeContext2 是否相等。如果它们是不相等的，就在构建工具层面修复这个问题。
### 尽管设置了不一样的默认值，但是我总是从 context 中得到 undefined
你可能在组件树中有一个没有设置 value 的 provider：
```
// 🚩 不起作用：没有 value 作为 prop<ThemeContext>   <Button /></ThemeContext>
```
如果你忘记了指定 value，它会像这样传值 value={undefined}。
你可能还错误地使用了一个不同的 prop 名：
```
// 🚩 不起作用：prop 应该是“value”<ThemeContext theme={theme}>   <Button /></ThemeContext>
```
在这两种情况下，你都应该在控制台中看到 React 发出的警告。要解决这些问题，使用 value 作为 prop：
```
// ✅ 传递 value 作为 prop<ThemeContext value={theme}>   <Button /></ThemeContext>
```
注意，只有在 上层根本没有匹配的 provider 时才使用 createContext(defaultValue)调用的默认值。如果存在 <SomeContext value={undefined}> 组件在父树的某个位置，调用 useContext(SomeContext) 的组件 将会 接收到 undefined 作为 context 的值。