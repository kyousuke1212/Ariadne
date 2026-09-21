API 参考过时的 React API Copy pageCopy
# isValidElement
isValidElement 检测参数值是否为 React 元素。
```
const isElement = isValidElement(value)
```
参考
- isValidElement(value)
用法
- 检测某些值是否是 React 元素
## 参考
### isValidElement(value)
调用 isValidElement(value) 来检测 value 是否是 React 元素。
```
import { isValidElement, createElement } from 'react';// ✅ React 元素console.log(isValidElement(<p />)); // trueconsole.log(isValidElement(createElement('p'))); // true// ❌ 非 React 元素console.log(isValidElement(25)); // falseconsole.log(isValidElement('Hello')); // falseconsole.log(isValidElement({ age: 42 })); // false
```
请看下方更多示例。
#### 参数
- value：你想要检测的 value 值。它可以是任何类型的值。
#### 返回值
如果 value 是一个 React 元素，isValidElement 返回 true；否则返回 false。
#### 注意事项
- 只有通过 createElement 返回的 JSX 标签 和对象会被认为是 React 元素。例如，即使像 42 这样的数字是一个有效的 React 节点（并且能从一个组件中返回），但它仍然不是有效的 React 元素。使用 createPortal 创建的数组和 portal 也 不被 认为是 React 元素。
## 用法
### 检测某些值是否是 React 元素
调用 isValidElement 来检测某个值是否是一个 React 元素。
React 元素指的是：
- 通过 JSX 标签 产生的值
- 通过调用 createElement 产生的值
对于 React 元素来说，isValidElement 返回 true：
```
import { isValidElement, createElement } from 'react';// ✅ JSX 标签是 React 元素console.log(isValidElement(<p />)); // trueconsole.log(isValidElement(<MyComponent />)); // true// ✅ 通过 createElement 返回的值是 React 元素console.log(isValidElement(createElement('p'))); // trueconsole.log(isValidElement(createElement(MyComponent))); // true
```
其他任意值，例如字符串，数字或者任意对象和数组等都不是 React 元素。
对于他们来说，isValidElement 返回值为 false：
```
// ❌ 这些 **不是** React 元素console.log(isValidElement(null)); // falseconsole.log(isValidElement(25)); // falseconsole.log(isValidElement('Hello')); // falseconsole.log(isValidElement({ age: 42 })); // falseconsole.log(isValidElement([<div />, <div />])); // falseconsole.log(isValidElement(MyComponent)); // false
```
需要用到 isValidElement 的场景并不常见。如果你调用另外一个 API，它 只 接受元素（像 cloneElement 那样），并且你想在参数不是 React 元素时避免报错，则这个方法是最有用的。
除非你有某些特定的原因需要添加 isValidElement 检测，否则不需要使用。
深入探讨
#### React 元素 vs React 节点
显示更多
当你编写组件时，你可以从中返回任意类型的 React 节点：
```
function MyComponent() {  // ... 你可以返回任何 React 节点 ...}
```
React 节点可能是：
- 像 <div /> 或者 createElement('div') 这样被创建的 React 元素
- 使用 createPortal 创建的 portal
- 字符串
- 数字
- true、false、null 或者 undefined（不会被展示出来）
- 其他 React 节点的数组
注意 isValidElement 只能检测参数是否为 React 元素，而不能检测它是否是 React 节点。例如 42 不是一个有效的 React 元素，但它是一个有效的 React 节点：
```
function MyComponent() {  return 42; // 从组件返回一个数字是没问题的}
```
这就是为什么你不应该用 isValidElement 来检测某些东西是否可以被渲染。