学习 React添加交互 Copy pageCopy
# 渲染和提交
组件显示到屏幕之前，其必须被 React 渲染。理解这些处理步骤将帮助你思考代码的执行过程并能解释其行为。
### 你将会学习到
- 在 React 中渲染的含义是什么
- 为什么以及什么时候 React 会渲染一个组件
- 在屏幕上显示组件所涉及的步骤
- 为什么渲染并不一定会导致 DOM 更新
想象一下，你的组件是厨房里的厨师，把食材烹制成美味的菜肴。在这种场景下，React 就是一名服务员，他会帮客户们下单并为他们送来所点的菜品。这种请求和提供 UI 的过程总共包括三个步骤：
- 触发 一次渲染（把客人的点单分发到厨房）
- 渲染 组件（在厨房准备订单）
- 提交 到 DOM（将菜品放在桌子上）
- 触发
- 渲染
- 提交
Rachel Lee Nabors 绘图
## 步骤 1: 触发一次渲染
有两种原因会导致组件的渲染:
- 组件的 初次渲染。
- 组件（或者其祖先之一）的 状态发生了改变。
### 初次渲染
当应用启动时，会触发初次渲染。框架和沙箱有时会隐藏这部分代码，但它是通过调用 createRoot 方法并传入目标 DOM 节点，然后用你的组件调用 render 函数完成的：
```
index.jsImage.jsindex.jsReloadClearForkimport Image from './Image.js';
import { createRoot } from 'react-dom/client';

const root = createRoot(document.getElementById('root'))
root.render(<Image />);
```
试着注释掉 root.render()，然后你将会看到组件消失。
### 状态更新时重新渲染
一旦组件被初次渲染，你就可以通过使用 set 函数 更新其状态来触发之后的渲染。更新组件的状态会自动将一次渲染送入队列。（你可以把这种情况想象成餐厅客人在第一次下单之后又点了茶、点心和各种东西，具体取决于他们的胃口。）
- 状态更新...
- ...触发...
- ...渲染!
Rachel Lee Nabors 绘图
## 步骤 2: React 渲染你的组件
在你触发渲染后，React 会调用你的组件来确定要在屏幕上显示的内容。“渲染中” 即 React 在调用你的组件。
- 在进行初次渲染时, React 会调用根组件。
- 对于后续的渲染, React 会调用内部状态更新触发了渲染的函数组件。
这个过程是递归的：如果更新后的组件会返回某个另外的组件，那么 React 接下来就会渲染 那个 组件，而如果那个组件又返回了某个组件，那么 React 接下来就会渲染 那个 组件，以此类推。这个过程会持续下去，直到没有更多的嵌套组件并且 React 确切知道哪些东西应该显示到屏幕上为止。
在接下来的例子中，React 将会调用 Gallery() 和 Image() 若干次：
```
index.jsGallery.jsGallery.jsReloadClearForkexport default function Gallery() {
  return (
    <section>
      <h1>鼓舞人心的雕塑</h1>
      <Image />
      <Image />
      <Image />
    </section>
  );
}

function Image() {
  return (
    <img
      src="https://react.dev/images/docs/scientists/ZF6s192.jpg"
      alt="'Floralis Genérica' by Eduardo Catalano: a gigantic metallic flower sculpture with reflective petals"
    />
  );
}
```
显示更多
- 在初次渲染中， React 将会为<section>、<h1> 和三个 <img> 标签 创建 DOM 节点。
- 在一次重渲染过程中, React 将计算它们的哪些属性（如果有的话）自上次渲染以来已更改。在下一步（提交阶段）之前，它不会对这些信息执行任何操作。
### 陷阱
渲染必须始终是一次 纯计算:
- 输入相同，输出相同。 给定相同的输入，组件应始终返回相同的 JSX。（当有人点了西红柿沙拉时，他们不应该收到洋葱沙拉！）
- 只做它自己的事情。 它不应更改任何存在于渲染之前的对象或变量。（一个订单不应更改其他任何人的订单。）
否则，随着代码库复杂性的增加，你可能会遇到令人困惑的错误和不可预测的行为。在 “严格模式” 下开发时，React 会调用每个组件的函数两次，这可以帮助发现由不纯函数引起的错误。
深入探讨
#### 性能优化
显示更多
如果更新的组件在树中的位置非常高，渲染更新后的组件内部所有嵌套组件的默认行为将不会获得最佳性能。如果你遇到了性能问题，性能 章节描述了几种可选的解决方案 。不要过早进行优化！
## 步骤 3: React 把更改提交到 DOM 上
在渲染（调用）你的组件之后，React 将会修改 DOM。
- 对于初次渲染，React 会使用 appendChild() DOM API 将其创建的所有 DOM 节点放在屏幕上。
- 对于重渲染，React 将应用最少的必要操作（在渲染时计算！），以使得 DOM 与最新的渲染输出相互匹配。
React 仅在渲染之间存在差异时才会更改 DOM 节点。 例如，有一个组件，它每秒使用从父组件传递下来的不同属性重新渲染一次。注意，你可以添加一些文本到 <input> 标签，更新它的 value，但是文本不会在组件重渲染时消失：
```
Clock.jsClock.jsReloadClearForkexport default function Clock({ time }) {
  return (
    <>
      <h1>{time}</h1>
      <input />
    </>
  );
}
```
这个例子之所以会正常运行，是因为在最后一步中，React 只会使用最新的 time 更新 <h1> 标签的内容。它看到 <input> 标签出现在 JSX 中与上次相同的位置，因此 React 不会修改 <input> 标签或它的 value！
## 尾声：浏览器绘制
在渲染完成并且 React 更新 DOM 之后，浏览器就会重新绘制屏幕。尽管这个过程被称为“浏览器渲染”（“browser rendering”），但我们还是将它称为“绘制”（“painting”），以避免在这些文档的其余部分中出现混淆。
Rachel Lee Nabors 绘图
## 摘要
在一个 React 应用中一次屏幕更新都会发生以下三个步骤：
- 触发
- 渲染
- 提交
- 你可以使用严格模式去找到组件中的错误
- 如果渲染结果与上次一样，那么 React 将不会修改 DOM