API 参考过时的 React API Copy pageCopy
# cloneElement
### 陷阱
使用 cloneElement 并不常见，并且可能会导致代码变得脆弱。查看常见的替代方案。
cloneElement 允许你使用一个元素作为初始值创建一个新的 React 元素。
```
const clonedElement = cloneElement(element, props, ...children)
```
参考
- cloneElement(element, props, ...children)
用法
- 覆盖元素的 props
替代方案
- 通过 props 传递数据
- 通过 context 传递数据
- 将逻辑提取到自定义 Hook 中
## 参考
### cloneElement(element, props, ...children)
调用 cloneElement 方法会基于 element 创建一个新的 React 元素，但新元素具有不同的 props 和 children：
```
import { cloneElement } from 'react';// ...const clonedElement = cloneElement(  <Row title="Cabbage">    Hello  </Row>,  { isHighlighted: true },  'Goodbye');console.log(clonedElement); // <Row title="Cabbage" isHighlighted={true}>Goodbye</Row>
```
请参阅下面的更多示例。
#### 参数
element：element 参数必须是一个有效的 React 元素。例如，它可以是一个类似 <Something /> 这样的 JSX 节点，也可以是 createElement 调用的结果，或者也可以是另一个 cloneElement 调用的结果。
props：props 参数必须是一个对象或 null。如果传 null，克隆后的元素将保留所有原始的 element.props。否则，对于 props 对象中的每个 prop 属性，返回的元素将“优先”使用 props 中的值而不是 element.props 中的值。其余的 props 将从原始的 element.props 中填充。如果你传递 props.key 或者 props.ref，它们将替换原来的。
可选 ...children：零个或多个子节点。它们可以是任何 React 节点，包括 React 元素、字符串、数字、portals、空节点（null、undefined、true 和 false），和 React 元素数组。如果你不传递任何 ...children 参数，则原始的 element.props.children 将被保留。
#### 返回值
cloneElement 返回一个具有一些属性的 React element 对象：
- type：与 element.type 相同。
- props：将 element.props 与你传递的 props 浅合并的结果。
- ref：原始的 element.ref，除非它被 props.ref 覆盖。
- key：原始的 element.key，除非它被 props.key 覆盖。
通常，你将从组件返回该元素或使其成为另一个元素的子元素。尽管你可以读取元素的属性，但最好在创建每个元素后将其视为不透明的，并且仅渲染它。
#### 注意事项
克隆一个元素 不会修改原始元素。
如果已知 children 是静态的，则你应该 将它们作为多个参数传递给 cloneElement，例如 cloneElement(element, null, child1, child2, child3)。如果你的 children 是动态的，请将整个数组作为第三个参数传递：cloneElement(element, null, listItems)。这确保了 React 会对任何动态列表 警告你缺少“key”，对于静态的列表，这是不必要的，因为它们不会重新排序。
cloneElement 会使得跟踪数据流向变得更加困难，所以请 尝试使用 替代方案。
## 用法
### 覆盖元素的 props
要覆盖某些 React element 的 props，请将其与 要覆盖的 props 一起传递给 cloneElement：
```
import { cloneElement } from 'react';// ...const clonedElement = cloneElement(  <Row title="Cabbage" />,  { isHighlighted: true });
```
在这里，生成的 克隆 element 将为 <Row title="Cabbage" isHighlighted={true} />。
让我们看一个示例，看看它什么时候有用。
想象一个 List 组件将其 children 渲染为可选择行的列表，并带有可更改的“下一步”按钮选择了哪一行。List 组件需要以不同的方式渲染所选的 Row，因此它克隆它收到的每个 <Row> 子级，并添加额外的 isHighlighted: true 或 isHighlighted: false 属性：
```
export default function List({ children }) {  const [selectedIndex, setSelectedIndex] = useState(0);  return (    <div className="List">      {Children.map(children, (child, index) =>        cloneElement(child, {          isHighlighted: index === selectedIndex        })      )}
```
假设 List 收到的原始 JSX 如下所示：
```
<List>  <Row title="Cabbage" />  <Row title="Garlic" />  <Row title="Apple" /></List>
```
通过克隆其 children，List 可以将额外的信息传递给内部的每个 Row。结果如下：
```
<List>  <Row    title="Cabbage"    isHighlighted={true}  />  <Row    title="Garlic"    isHighlighted={false}  />  <Row    title="Apple"    isHighlighted={false}  /></List>
```
注意点击“下一步”如何更新 List 的状态，并高亮显示不同的行：
```
App.jsList.jsRow.jsdata.jsList.jsReloadClearForkimport { Children, cloneElement, useState } from 'react';

export default function List({ children }) {
  const [selectedIndex, setSelectedIndex] = useState(0);
  return (
    <div className="List">
      {Children.map(children, (child, index) =>
        cloneElement(child, {
          isHighlighted: index === selectedIndex
        })
      )}
      <hr />
      <button onClick={() => {
        setSelectedIndex(i =>
          (i + 1) % Children.count(children)
        );
      }}>
        下一步
      </button>
    </div>
  );
}
```
显示更多
总而言之，List 克隆了它接收的 <Row /> 元素，并向它们添加额外的 props。
### 陷阱
克隆 children 使得你很难判断数据如何流经你的应用。尝试一种 替代方案。
## 替代方案
### 通过 props 传递数据
接受类似 renderItem 这样的 render prop 代替 cloneElement 的用法。在这里，List 接收 renderItem 作为 props。List 为数组每一项调用 renderItem，并传递 isHighlighted 作为参数：
```
export default function List({ items, renderItem }) {  const [selectedIndex, setSelectedIndex] = useState(0);  return (    <div className="List">      {items.map((item, index) => {        const isHighlighted = index === selectedIndex;        return renderItem(item, isHighlighted);      })}
```
renderItem 属性称为“渲染属性”，因为它是决定如何渲染某些内容的属性。例如，你可以传递一个 renderItem 实现使用给定的 isHighlighted 值呈现 <Row>：
```
<List  items={products}  renderItem={(product, isHighlighted) =>    <Row      key={product.id}      title={product.title}      isHighlighted={isHighlighted}    />  }/>
```
最终结果与 cloneElement 相同：
```
<List>  <Row    title="Cabbage"    isHighlighted={true}  />  <Row    title="Garlic"    isHighlighted={false}  />  <Row    title="Apple"    isHighlighted={false}  /></List>
```
但是你可以清楚地追踪 isHighlighted 的来源。
```
App.jsList.jsRow.jsdata.jsList.jsReloadClearForkimport { useState } from 'react';

export default function List({ items, renderItem }) {
  const [selectedIndex, setSelectedIndex] = useState(0);
  return (
    <div className="List">
      {items.map((item, index) => {
        const isHighlighted = index === selectedIndex;
        return renderItem(item, isHighlighted);
      })}
      <hr />
      <button onClick={() => {
        setSelectedIndex(i =>
          (i + 1) % items.length
        );
      }}>
        下一步
      </button>
    </div>
  );
}
```
显示更多
这种方案优于 cloneElement，因为它更加清晰。
### 通过 context 传递数据
cloneElement 的另一种替代方法是 通过 context 传递数据。
例如，你可以调用 createContext 来定义一个 HighlightContext：
```
export const HighlightContext = createContext(false);
```
List 组件可以将其呈现的每个 item 传递到 HighlightContext provider 中：
```
export default function List({ items, renderItem }) {  const [selectedIndex, setSelectedIndex] = useState(0);  return (    <div className="List">      {items.map((item, index) => {        const isHighlighted = index === selectedIndex;        return (          <HighlightContext key={item.id} value={isHighlighted}>            {renderItem(item)}          </HighlightContext>        );      })}
```
通过这种方法，Row 不需要接收 isHighlighted属性，因为它可以从 context 中读取：
```
export default function Row({ title }) {  const isHighlighted = useContext(HighlightContext);  // ...
```
这允许调用组件时无需关心是否将 isHighlighted 传递给了 <Row>：
```
<List  items={products}  renderItem={product =>    <Row title={product.title} />  }/>
```
相反，List 和 Row 通过上下文协调突出显示逻辑。
```
App.jsList.jsRow.jsHighlightContext.jsdata.jsList.jsReloadClearForkimport { useState } from 'react';
import { HighlightContext } from './HighlightContext.js';

export default function List({ items, renderItem }) {
  const [selectedIndex, setSelectedIndex] = useState(0);
  return (
    <div className="List">
      {items.map((item, index) => {
        const isHighlighted = index === selectedIndex;
        return (
          <HighlightContext
            key={item.id}
            value={isHighlighted}
          >
            {renderItem(item)}
          </HighlightContext>
        );
      })}
      <hr />
      <button onClick={() => {
        setSelectedIndex(i =>
          (i + 1) % items.length
        );
      }}>
        下一步
      </button>
    </div>
  );
}
```
显示更多
了解有关通过 context 传递数据的更多信息。
### 将逻辑提取到自定义 Hook 中
你可以尝试的另一种方法是将“非视觉”部分的逻辑提取到你的自定义 Hook 中，并使用 Hook 的返回值来决定渲染什么。例如，你可以编写一个 useList 自定义 Hook，如下所示：
```
import { useState } from 'react';export default function useList(items) {  const [selectedIndex, setSelectedIndex] = useState(0);  function onNext() {    setSelectedIndex(i =>      (i + 1) % items.length    );  }  const selected = items[selectedIndex];  return [selected, onNext];}
```
然后你可以像这样使用它：
```
export default function App() {  const [selected, onNext] = useList(products);  return (    <div className="List">      {products.map(product =>        <Row          key={product.id}          title={product.title}          isHighlighted={selected === product}        />      )}      <hr />      <button onClick={onNext}>        下一步      </button>    </div>  );}
```
数据流是显式的，但状态位于 useList 自定义 Hook 内，你可以在任意一个组件内使用它：
```
App.jsuseList.jsRow.jsdata.jsApp.jsReloadClearForkimport Row from './Row.js';
import useList from './useList.js';
import { products } from './data.js';

export default function App() {
  const [selected, onNext] = useList(products);
  return (
    <div className="List">
      {products.map(product =>
        <Row
          key={product.id}
          title={product.title}
          isHighlighted={selected === product}
        />
      )}
      <hr />
      <button onClick={onNext}>
        下一步
      </button>
    </div>
  );
}
```
显示更多
如果你想在不同组件之间复用此逻辑，则这个方案十分有用。