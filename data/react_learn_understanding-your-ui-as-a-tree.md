学习 React描述 UI Copy pageCopy
# 将 UI 视为树
当 React 应用程序逐渐成形时，许多组件会出现嵌套。那么 React 是如何跟踪应用程序组件结构的？
React 以及许多其他 UI 库，将 UI 建模为树。将应用程序视为树对于理解组件之间的关系以及调试性能和状态管理等未来将会遇到的一些概念非常有用。
### 你将会学习到
- React 如何看待组件结构
- 渲染树是什么以及它有什么用处
- 模块依赖树是什么以及它有什么用处
## 将 UI 视为树
树是项目和 UI 之间的关系模型，通常使用树结构来表示 UI。例如，浏览器使用树结构来建模 HTML（DOM）与CSS（CSSOM）。移动平台也使用树来表示其视图层次结构。
React 从组件中创建 UI 树。在这个示例中，UI 树最后会用于渲染 DOM。
与浏览器和移动平台一样，React 还使用树结构来管理和建模 React 应用程序中组件之间的关系。这些树是有用的工具，用于理解数据如何在 React 应用程序中流动以及如何优化呈现和应用程序大小。
## 渲染树
组件的一个主要特性是能够由其他组件组合而成。在 嵌套组件 中有父组件和子组件的概念，其中每个父组件本身可能是另一个组件的子组件。
当渲染 React 应用程序时，可以在一个称为渲染树的树中建模这种关系。
下面的 React 应用程序渲染了一些鼓舞人心的引语。
```
App.jsFancyText.jsInspirationGenerator.jsCopyright.jsquotes.jsApp.jsReloadClearForkimport FancyText from './FancyText';
import InspirationGenerator from './InspirationGenerator';
import Copyright from './Copyright';

export default function App() {
  return (
    <>
      <FancyText title text="Get Inspired App" />
      <InspirationGenerator>
        <Copyright year={2004} />
      </InspirationGenerator>
    </>
  );
}
```
React 创建的 UI 树是由渲染过的组件构成的，被称为渲染树。
通过示例应用程序，可以构建上面的渲染树。
这棵树由节点组成，每个节点代表一个组件。例如，App、FancyText、Copyright 等都是我们树中的节点。
在 React 渲染树中，根节点是应用程序的 根组件。在这种情况下，根组件是 App，它是 React 渲染的第一个组件。树中的每个箭头从父组件指向子组件。
深入探讨
#### 那么渲染树中的 HTML 标签在哪里呢？
显示更多
也许会注意到在上面的渲染树中，没有提到每个组件渲染的 HTML 标签。这是因为渲染树仅由 React 组件 组成。
React 是跨平台的 UI 框架。react.dev 展示了一些渲染到使用 HTML 标签作为 UI 原语的 web 的示例。但是 React 应用程序同样可以渲染到移动设备或桌面平台，这些平台可能使用不同的 UI 原语，如 UIView 或 FrameworkElement。
这些平台 UI 原语不是 React 的一部分。无论应用程序渲染到哪个平台，React 渲染树都可以为 React 应用程序提供见解。
渲染树表示 React 应用程序的单个渲染过程。在 条件渲染 中，父组件可以根据传递的数据渲染不同的子组件。
我们可以更新应用程序以有条件地渲染励志语录或颜色。
```
App.jsFancyText.jsColor.jsInspirationGenerator.jsCopyright.jsinspirations.jsApp.jsReloadClearForkimport FancyText from './FancyText';
import InspirationGenerator from './InspirationGenerator';
import Copyright from './Copyright';

export default function App() {
  return (
    <>
      <FancyText title text="Get Inspired App" />
      <InspirationGenerator>
        <Copyright year={2004} />
      </InspirationGenerator>
    </>
  );
}
```
在条件渲染的不同渲染过程中，渲染树可能会渲染不同的组件。
在这个示例中，根据 inspiration.type 的值可能会渲染 <FancyText> 或 <Color>。每次渲染过程的渲染树可能都不同。
尽管渲染树可能在不同的渲染过程中有所不同，但通常这些树有助于识别 React 应用程序中的顶级和叶子组件。顶级组件是离根组件最近的组件，它们影响其下所有组件的渲染性能，通常包含最多复杂性。叶子组件位于树的底部，没有子组件，通常会频繁重新渲染。
识别这些组件类别有助于理解应用程序的数据流和性能。
## 模块依赖树
在 React 应用程序中，可以使用树来建模的另一个关系是应用程序的模块依赖关系。当 拆分组件 和逻辑到不同的文件中时，就创建了 JavaScript 模块，在这些模块中可以导出组件、函数或常量。
模块依赖树中的每个节点都是一个模块，每个分支代表该模块中的 import 语句。
以之前的 Inspirations 应用程序为例，可以构建一个模块依赖树，简称依赖树。
Inspirations 应用程序的模块依赖树。
树的根节点是根模块，也称为入口文件。它通常包含根组件的模块。
与同一应用程序的渲染树相比，存在相似的结构，但也有一些显著的差异：
- 构成树的节点代表模块，而不是组件。
- 非组件模块，如 inspirations.js，在这个树中也有所体现。渲染树仅封装组件。
- Copyright.js 出现在 App.js 下，但在渲染树中，Copyright 作为 InspirationGenerator 的子组件出现。这是因为 InspirationGenerator 接受 JSX 作为 children props，因此它将 Copyright 作为子组件渲染，但不导入该模块。
依赖树对于确定运行 React 应用程序所需的模块非常有用。在为生产环境构建 React 应用程序时，通常会有一个构建步骤，该步骤将捆绑所有必要的 JavaScript 以供客户端使用。负责此操作的工具称为 bundler（捆绑器），并且 bundler 将使用依赖树来确定应包含哪些模块。
随着应用程序的增长，捆绑包大小通常也会增加。大型捆绑包大小对于客户端来说下载和运行成本高昂，并延迟 UI 绘制的时间。了解应用程序的依赖树可能有助于调试这些问题。
## 摘要
- 树是表示实体之间关系的常见方式，它们经常用于建模 UI。
- 渲染树表示单次渲染中 React 组件之间的嵌套关系。
- 使用条件渲染，渲染树可能会在不同的渲染过程中发生变化。使用不同的属性值，组件可能会渲染不同的子组件。
- 渲染树有助于识别顶级组件和叶子组件。顶级组件会影响其下所有组件的渲染性能，而叶子组件通常会频繁重新渲染。识别它们有助于理解和调试渲染性能问题。
- 依赖树表示 React 应用程序中的模块依赖关系。
- 构建工具使用依赖树来捆绑必要的代码以部署应用程序。
- 依赖树有助于调试大型捆绑包带来的渲染速度过慢的问题，以及发现哪些捆绑代码可以被优化。