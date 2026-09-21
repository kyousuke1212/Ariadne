API 参考Lints Copy pageCopy
# immutability
验证是否修改了 props、state 和其它 不可变 的值。
## 规则详情
组件的 props 和 state 是不可变的快照。永远不要直接修改它们。相反，应向下传递新的 props，并使用 useState 提供的 setter 函数。
## 常见违规示例
### 无效的
```
// ❌ 数组 push 修改function Component() {  const [items, setItems] = useState([1, 2, 3]);  const addItem = () => {    items.push(4); // 修改！    setItems(items); // 引用相同，不重新渲染  };}// ❌ 对象属性赋值function Component() {  const [user, setUser] = useState({name: 'Alice'});  const updateName = () => {    user.name = 'Bob'; // 修改！    setUser(user); // 引用相同  };}// ❌ 未利用展开进行排序function Component() {  const [items, setItems] = useState([3, 1, 2]);  const sortItems = () => {    setItems(items.sort()); // sort 会修改原数组！  };}
```
### 有效的
```
// ✅ 创建新数组function Component() {  const [items, setItems] = useState([1, 2, 3]);  const addItem = () => {    setItems([...items, 4]); // 新数组  };}// ✅ 创建新对象function Component() {  const [user, setUser] = useState({name: 'Alice'});  const updateName = () => {    setUser({...user, name: 'Bob'}); // 新对象  };}
```
## 故障排除
### 我需要向数组添加项
使用 push() 之类的方法修改数组不会触发重新渲染：
```
// ❌ 错误：修改数组function TodoList() {  const [todos, setTodos] = useState([]);  const addTodo = (id, text) => {    todos.push({id, text});    setTodos(todos); // 相同的数组引用！  };  return (    <ul>      {todos.map(todo => <li key={todo.id}>{todo.text}</li>)}    </ul>  );}
```
改为创建一个新数组：
```
// ✅ 更好的做法：创建新数组function TodoList() {  const [todos, setTodos] = useState([]);  const addTodo = (id, text) => {    setTodos([...todos, {id, text}]);    // 或者：setTodos(todos => [...todos, {id: Date.now(), text}])  };  return (    <ul>      {todos.map(todo => <li key={todo.id}>{todo.text}</li>)}    </ul>  );}
```
### 我需要更新嵌套对象
修改嵌套属性不会触发重新渲染：
```
// ❌ 错误：修改嵌套对象function UserProfile() {  const [user, setUser] = useState({    name: 'Alice',    settings: {      theme: 'light',      notifications: true    }  });  const toggleTheme = () => {    user.settings.theme = 'dark'; // 修改！    setUser(user); // 相同的对象引用  };}
```
在需要更新的每一层级进行展开：
```
// ✅ 更好的做法：在每一层级创建新对象function UserProfile() {  const [user, setUser] = useState({    name: 'Alice',    settings: {      theme: 'light',      notifications: true    }  });  const toggleTheme = () => {    setUser({      ...user,      settings: {        ...user.settings,        theme: 'dark'      }    });  };}
```