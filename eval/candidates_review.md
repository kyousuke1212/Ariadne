# 评测问题候选 · 人工确认表

规则：每条问题，把【能完整回答它的所有块】勾上（可多选），其余不勾。
默认已勾了生成源块（问题就是从它生成的，一般都对）；
重点看备选池里有没有【同样能回答】的块，有就勾上；
如果问题本身不合格（太泛/答案不在语料），把整条划掉或标注「删」。

### 1. [命名精确] "use no memo" 这个指令应该写在什么位置才能生效？

- [x] react_reference_react-compiler_directives_use-no-memo.md-2  —  ata }) { "use no memo"; // TODO: 修复 issue #123 后移除 // 未被静态检测到的违反 React 规则的代码 // ...} ``` #### 第三方库集成
- [ ] react_reference_react-compiler_directives.md-3  —  mpilationMode: 'infer' }] ]}// ⚠️ 仅在必要时使用指令function SpecialCase() { "use no memo"; // 务必注释说明为何需要这样做 
- [ ] react_reference_react-compiler_directives.md-4  —  ; // TODO: 待 ThirdPartyLib 升级到 v2.0 后移除 return <ThirdPartyComponent />;} ``` ## 常见模式 ### 渐进式引入 在大型代码
- [ ] react_reference_react-compiler_directives_use-memo.md-0  —  API 参考指令 Copy pageCopy # use memo "use memo" 用于标记一个函数，以便 React 编译器对其进行优化。 ### 注意 在大多数情况下，你并不需要使用 "us
- [ ] react_reference_react-compiler_directives_use-no-memo.md-0  —  API 参考指令 Copy pageCopy # use no memo "use no memo" 可以防止函数被 React 编译器优化。 参考 - "use no memo" - "use no
- [ ] react_reference_react-compiler_directives_use-no-memo.md-1  —  反引号。 - 该指令必须与 "use no memo" 或其别名 "use no forget" 完全匹配。 - 该指令的优先级高于所有编译模式和其他指令。 - 它旨在作为一种临时的调试工具，而非永久
- [ ] react_reference_react-compiler_directives_use-no-memo.md-3  —  未阻止编译 如果 "use no memo" 不起作用： ``` // ❌ 错误 - 指令在代码之后function Component() { const data = getData(); "us

### 2. [语义改写] 当函数级和模块级都写了 "use no memo" 时，哪个的优先级更高？

- [x] react_reference_react-compiler_directives_use-no-memo.md-2  —  ata }) { "use no memo"; // TODO: 修复 issue #123 后移除 // 未被静态检测到的违反 React 规则的代码 // ...} ``` #### 第三方库集成
- [ ] react_reference_react-compiler_directives.md-0  —  API 参考 Copy pageCopy # 指令 React 编译器指令是特殊的字符串文字，用于控制特定函数是否被编译。 ``` function MyComponent() { "use memo
- [ ] react_reference_react-compiler_directives.md-1  —  强制编译 | 当使用 annotation 模式时，或需要覆盖 infer 模式的推断逻辑时 | "use no memo" | 阻止编译 | 调试问题或处理不兼容的代码时 | ## 用法 ### 函
- [ ] react_reference_react-compiler_directives_use-memo.md-0  —  API 参考指令 Copy pageCopy # use memo "use memo" 用于标记一个函数，以便 React 编译器对其进行优化。 ### 注意 在大多数情况下，你并不需要使用 "us
- [ ] react_reference_react-compiler_directives_use-memo.md-2  —  式地标记一个函数需要被优化，从而覆盖编译器的默认行为： - 在 annotation 模式下：只有带 "use memo" 的函数才会被优化 - 在 infer 模式下：编译器使用启发式规则进行推断，
- [ ] react_reference_react-compiler_directives_use-no-memo.md-0  —  API 参考指令 Copy pageCopy # use no memo "use no memo" 可以防止函数被 React 编译器优化。 参考 - "use no memo" - "use no
- [ ] react_reference_react-compiler_directives_use-no-memo.md-1  —  反引号。 - 该指令必须与 "use no memo" 或其别名 "use no forget" 完全匹配。 - 该指令的优先级高于所有编译模式和其他指令。 - 它旨在作为一种临时的调试工具，而非永久
- [ ] react_reference_react_PureComponent.md-8  —  > </> ); } ``` 显示更多 ### 注意 与 PureComponent 不同，memo 不会比较新旧 state。在函数组件中，即使没有 memo，调用具有相同 state 的 set 

### 3. [语义改写] 在 JSX 里想要把一个对象作为属性值传进去，需要用什么方式包裹这个对象？

- [x] react_learn_javascript-in-jsx-with-curly-braces.md-5  —  }。因此，为了能在 JSX 中传递，你必须用另一对额外的大括号包裹对象：person={{ name: "Hedy Lamarr", inventions: 5 }}。 你可能在 JSX 的内联 CS
- [ ] react_learn_describing-the-ui.md-7  —  e alcohol-fuelled engine</li> </ul> </div> ); } ``` 显示更多 ## 想要仔细学习这个主题的内容吗？ 请参阅 在 JSX 中通过大括号使用 JavaS
- [ ] react_learn_describing-the-ui.md-9  —  想要仔细学习这个主题的内容吗？ 请参阅 将 Props 传递给组件 以了解如何传递并读取 props。 阅读更多 ## 条件渲染 你的组件经常需要根据不同的条件来显示不同的东西。在 React 中，你
- [ ] react_learn_manipulating-the-dom-with-refs.md-1  —  ``` const myRef = useRef(null); ``` 最后，将 ref 作为 ref 属性值传递给想要获取的 DOM 节点的 JSX 标签： ``` <div ref={myRef}
- [ ] react_learn_rendering-lists.md-8  —  rson.id}>...</li> ``` ### 注意 直接放在 map() 方法里的 JSX 元素一般都需要指定 key 值！ 这些 key 会告诉 React，每个组件对应着数组里的哪一项，所以
- [ ] react_learn_rendering-lists.md-12  —  下，假如你桌面上的文件都没有文件名，取而代之的是，你需要通过文件的位置顺序来区分它们———第一个文件，第二个文件，以此类推。也许你也不是不能接受这种方式，可是一旦你删除了其中的一个文件，这种组织方式就
- [ ] react_learn_updating-objects-in-state.md-28  —  。 - 需求变更：有些应用功能在不出现任何修改的情况下会更容易实现，比如实现撤销/恢复、展示修改历史，或是允许用户把表单重置成某个之前的值。这是因为你可以把 state 之前的拷贝保存到内存中，并适时
- [ ] react_learn_writing-markup-with-jsx.md-5  —  点。 深入探讨 #### 为什么多个 JSX 标签需要被一个父元素包裹？ 显示更多 JSX 虽然看起来很像 HTML，但在底层其实被转化为了 JavaScript 对象，你不能在一个函数中返回多个对象
- [ ] react_reference_react-dom_components.md-4  —  butes 传递： ``` <my-element value="Hello, world!"></my-element> ``` 默认情况下，传递给自定义元素的非字符串 JavaScript 值将被
- [ ] vue_guide_extras_render-function.md-16  —  得传递 null 以避免插槽被误认为 prop： js // 子组件 export default { setup(props, { slots }) { const text = ref('hi')

### 4. [命名精确] 在 React 中给元素添加内联样式时，应该向哪个属性传入一个对象？

- [x] react_learn_javascript-in-jsx-with-curly-braces.md-5  —  }。因此，为了能在 JSX 中传递，你必须用另一对额外的大括号包裹对象：person={{ name: "Hedy Lamarr", inventions: 5 }}。 你可能在 JSX 的内联 CS
- [ ] react_learn_typescript.md-19  —  ript 原始类型，如 string 或 number： ``` interface ModalRendererProps { title: string; children: React.React
- [ ] react_reference_react-dom_components_script.md-0  —  API 参考组件 Copy pageCopy # <script> 浏览器内置的 <script> 组件 允许向文档添加脚本。 ``` <script> alert("hi!") </script> 
- [ ] react_reference_react-dom_components_style.md-0  —  API 参考组件 Copy pageCopy # <style> 浏览器内置的 <style> 允许向文档添加内联 CSS 样式表。 ``` <style>{` p { color: red; } `
- [ ] react_reference_react-dom_components_style.md-2  —  同的样式表，并在样式表加载时 挂起。 请提供 href 和 precedence 属性以选择此行为。如果样式表具有相同的 href，React 将对样式去重。优先级属性告诉 React 在文档的 <h
- [ ] react_reference_react-dom_components_style.md-3  —  ，React 将根据这些值在组件树中出现的顺序对内联样式表重新排序。 内联样式表在加载时不会触发 Suspense 边界。 即使他们加载字体或图像等异步资源。 ``` App.jsShowRender
- [ ] vue_guide_essentials_class-and-style.md-5  —  ! This is a child component 你可以在透传 Attribute 一章中了解更多组件的 attribute 继承的细节。 ## 绑定内联样式 ### 绑定对象 :style 支

### 5. [语义改写] 当 InspirationGenerator 以 children 方式接收 Copyright 时，为什么说这两个组件之间并不存在直接的导入或调用关系？

- [x] react_reference_rsc_use-client.md-8  —  这种情况下，InspirationGenerator 以 children 的形式接收 Copyright。然而，InspirationGenerator 模块从未直接导入 Copyright 模块，
- [ ] react_learn_responding-to-events.md-17  —  {children} </button> );} ``` 你也可以在调用父元素 onClick 函数之前，向这个处理函数添加更多代码。此模式是事件传播的另一种 替代方案 。它让子组件处理事件，同时也让
- [ ] react_learn_understanding-your-ui-as-a-tree.md-5  —  染性能，通常包含最多复杂性。叶子组件位于树的底部，没有子组件，通常会频繁重新渲染。 识别这些组件类别有助于理解应用程序的数据流和性能。 ## 模块依赖树 在 React 应用程序中，可以使用树来建模的
- [ ] react_learn_understanding-your-ui-as-a-tree.md-6  —  树中，Copyright 作为 InspirationGenerator 的子组件出现。这是因为 InspirationGenerator 接受 JSX 作为 children props，因此它将 
- [ ] react_reference_react_Children.md-24  —  t(children) 的返回值仍然是 2。从 RowList 的角度上看，它只能感知到它直接接收到的 JSX，并不能感知到 MoreRows 组件的内部。 这导致抽离一个组件变得较为困难，这也是为什
- [ ] react_reference_rsc_use-client.md-6  —  `` import MyComponent from './MyComponent';function App() { // 这是组件的用法 return <MyComponent />;} ``` 
- [ ] react_reference_rsc_use-client.md-7  —  tor 包含 'use client' 指示符。 这意味着 FancyText 的组件定义将在服务器上进行评估，同时也将被客户端下载以渲染其客户端组件的使用。 深入探讨 #### 为什么 Copyri

### 6. [命名精确] 在 React 中，用什么指令来标记客户端组件，从而区别于默认的服务器组件？

- [x] react_reference_rsc_use-client.md-8  —  这种情况下，InspirationGenerator 以 children 的形式接收 Copyright。然而，InspirationGenerator 模块从未直接导入 Copyright 模块，
- [ ] react_reference_react.md-1  —  ient API 允许在客户端（浏览器中）渲染 React 组件。 - 服务端 API —— react-dom/server API 允许在服务器端将 React 组件渲染为 HTML。 - 静态 
- [ ] react_reference_rsc_use-client.md-0  —  API 参考指令符 Copy pageCopy # 'use client' ### React 服务器组件 'use client' 用于 React 服务器组件。 'use client' 标记在
- [ ] react_reference_rsc_use-client.md-2  —  件模块包含 'use client' 指示符时，保证对该组件的任何使用都将是客户端组件。然而，即使没有 'use client' 指示符，组件仍可以在客户端上进行评估。 - 如果组件是在带有 'use
- [ ] react_reference_rsc_use-client.md-4  —  nspirationGenerator> </> ); } ``` 在这个示例应用程序的模块依赖树中，InspirationGenerator.js 中的 'use client' 指示符标记了该模块
- [ ] react_reference_rsc_use-client.md-15  —  return <canvas ref={ref} />;} ``` ### 使用第三方库 在 React 应用程序中，通常会利用第三方库来处理常见的 UI 模式或逻辑。 这些库可能依赖于组件 Hook
- [ ] react_reference_rsc_use-server.md-0  —  API 参考指令符 Copy pageCopy # 'use server' ### React 服务器组件 'use server' 用于 React 服务器组件。 'use server' 标记可

### 7. [概念术语] 在 React 中调用 createContext 时传入一个参数作为默认值，这样做有什么好处？

- [x] react_reference_react_useContext.md-11  —  ThemeContext = createContext('light'); ``` 这样，如果你不小心渲染了没有相应 provider 的某个组件，它也不会出错。这也有助于你的组件在测试环境中很好地
- [ ] react_learn_passing-data-deeply-with-context.md-6  —  App.jsSection.jsHeading.jsLevelContext.jsLevelContext.jsReloadClearForkimport { createContext } from
- [ ] react_learn_passing-data-deeply-with-context.md-10  —  Section> </Section> </Section> </Section> ); } ``` 显示更多 注意！这个示例还不能运行。所有 headings 的尺寸都一样，因为 即使你正在使用 c
- [ ] react_learn_typescript.md-12  —  个合理的默认值情况下，这种技术是有效的。但是当你没有合理的默认值的时候，null 作为默认值可能感觉是合理的。但是为了让类型系统理解你的代码，你需要在 createContext 上显式设置 Cont
- [ ] react_reference_react-compiler_compiling-libraries.md-0  —  API 参考 Copy pageCopy # 编译库 本指南旨在帮助库作者理解如何使用 React 编译器来为用户提供经过优化的库代码。 - 为什么要发布编译后的代码？ - 设置编译 向下兼容性 - 
- [ ] react_reference_react_createContext.md-1  —  # 参数 - defaultValue：当读取上下文的组件上方的树中没有匹配的上下文时，希望该上下文具有的默认值。倘若没有任何有意义的默认值，可指定其为 null。该默认值是用于作为“最后的手段”的后
- [ ] react_reference_react_createContext.md-4  —  函数的返回值渲染结果。当来自父组件的上下文发生变化时，React 会重新调用该函数。 ## 使用方法 ### 创建上下文 上下文使得组件能够无需通过显式传递参数的方式 将信息逐层传递。 在任何组件外调
- [ ] react_reference_react_useContext.md-17  —  你可以通过 context 传递任何值，包括对象和函数。 ``` function MyApp() { const [currentUser, setCurrentUser] = useState(n
- [ ] react_reference_react_useContext.md-21  —  它会像这样传值 value={undefined}。 你可能还错误地使用了一个不同的 prop 名： ``` // 🚩 不起作用：prop 应该是“value”<ThemeContext theme=

### 8. [数字精确] 例子中 ThemeContext 的默认主题值是什么？

- [x] react_reference_react_useContext.md-11  —  ThemeContext = createContext('light'); ``` 这样，如果你不小心渲染了没有相应 provider 的某个组件，它也不会出错。这也有助于你的组件在测试环境中很好地
- [ ] react_learn_passing-data-deeply-with-context.md-6  —  App.jsSection.jsHeading.jsLevelContext.jsLevelContext.jsReloadClearForkimport { createContext } from
- [ ] react_learn_typescript.md-11  —  ight" | "dark" | "system"; const ThemeContext = createContext<Theme>("system"); const useGetTheme = 
- [ ] react_reference_react_createContext.md-5  —  ontext); // ...} ``` 默认情况下，它们将获得的值是你在创建上下文时指定的 默认值。然而，它本身并不是很有用，因为默认值永远不会发生改变。 上下文之所以有用，是因为可以 提供来自其他
- [ ] react_reference_react_useContext.md-14  —  同的值包装树的某个部分，可以覆盖该部分的 context。 ``` <ThemeContext value="dark"> ... <ThemeContext value="light"> <Foot
- [ ] vue_guide_extras_reactivity-in-dep.md-0  —  # 深入响应式系统 Vue 最标志性的功能就是其低侵入性的响应式系统。组件状态都是由响应式的 JavaScript 对象组成的。当更改它们时，视图会随即自动更新。这让状态管理更加简单直观，但理解它是如
- [ ] vue_guide_extras_reactivity-in-depth.md-0  —  # 深入响应式系统 Vue 最标志性的功能就是其低侵入性的响应式系统。组件状态都是由响应式的 JavaScript 对象组成的。当更改它们时，视图会随即自动更新。这让状态管理更加简单直观，但理解它是如

### 9. [概念术语] 为什么说污点标记不能作为唯一的安全保障？

- [x] react_reference_react_experimental_taintObjectReference.md-3  —  递给客户端组件这种简单的错误。 ### 陷阱 不要仅依赖于污点标记来确保安全。被污染的对象并不防止泄露每一个可能的派生值。例如，被污染的对象的克隆将创建一个新的未被污染的对象。使用来自被污染的对象的数
- [ ] react_learn_rendering-lists.md-11  —  /h1> <p>{person.bio}</p> </Fragment>); ``` 这里的 Fragment 标签本身并不会出现在 DOM 上，这串代码最终会转换成 <h1>、<p>、<h1>、<p
- [ ] react_reference_react-dom_components_common.md-50  —  ML。不建议像 <div dangerouslySetInnerHTML={{__html: markup}} /> 这样内联创建对象。 要了解为什么渲染任意 HTML 是危险的，请将上面的代码替换为
- [ ] react_reference_react_experimental_taintUniqueValue.md-2  —  递给客户端组件时显示的消息。如果将 value 传递给客户端组件，此消息将作为错误的一部分显示。 lifetime：指示 value 应该被污染多长时间的任何对象。只要此对象仍然存在，将阻止把 val
- [ ] react_reference_react_experimental_taintUniqueValue.md-5  —  r;} ``` 在此示例中，user 对象用作 lifetime 参数。如果此对象存储在全局缓存中或可以被其他请求访问，会话令牌将保持被污染的状态。 ### 陷阱 不要仅依赖于污点标记来确保安全。污染
- [ ] react_reference_react_experimental_taintUniqueValue.md-6  —  被污染。然后，通过在 password 上调用 toUpperCase 方法使用 password 创建新值 uppercasePassword。新创建的 uppercasePassword 不被污染
- [ ] vue_guide_best-practices_security.md-6  —  每个 HTML 元素都有能接受字符串形式 JavaScript 的 attribute，例如 onclick、onfocus 和 onmouseenter。绑定任何用户提供的 JavaScript 给

### 10. [命名精确] React 中用于污染用户对象的实验性 API 叫什么名字？

- [x] react_reference_react_experimental_taintObjectReference.md-3  —  递给客户端组件这种简单的错误。 ### 陷阱 不要仅依赖于污点标记来确保安全。被污染的对象并不防止泄露每一个可能的派生值。例如，被污染的对象的克隆将创建一个新的未被污染的对象。使用来自被污染的对象的数
- [ ] react_learn_understanding-your-ui-as-a-tree.md-3  —  act.dev 展示了一些渲染到使用 HTML 标签作为 UI 原语的 web 的示例。但是 React 应用程序同样可以渲染到移动设备或桌面平台，这些平台可能使用不同的 UI 原语，如 UIView
- [ ] react_reference_react-dom.md-2  —  r API 来替代。 - renderToStaticNodeStream：使用 react-dom/server API 来替代。
- [ ] react_reference_react_act.md-0  —  API 参考API Copy pageCopy # act act 是个测试辅助工具，用于在断言前应用待处理的 React 更新。 ``` await act(async actFn) ``` 要将组
- [ ] react_reference_react_experimental_taintObjectReference.md-0  —  API 参考API Copy pageCopy # experimental_taintObjectReference - This feature is available in the lates
- [ ] react_reference_react_experimental_taintObjectReference.md-2  —  显示的消息。如果对象被传递给客户端组件，此消息将作为错误的一部分显示。 object：被污染的对象。函数和类实例可以作为 object 传递给 taintObjectReference。React 会
- [ ] react_reference_react_experimental_taintUniqueValue.md-0  —  API 参考API Copy pageCopy # experimental_taintUniqueValue - This feature is available in the latest Ex
- [ ] react_reference_rsc_use-server.md-2  —  器函数的框架通常一次只处理一个 Action，没有缓存返回值的方式。 ### 安全考虑 服务器函数的参数完全由客户端控制。出于安全考虑，始终将它们视为不受信任的输入，并确保根据需要验证和转义参数。 在

### 11. [命名精确] 在 React 中，如果想让某个 option 呈现不可用且变暗的外观，应该设置哪个属性？

- [x] react_reference_react-dom_components_option.md-1  —  ops <option> 支持所有 常见的元素属性。 除此之外，<option> 还支持以下属性： - disabled：布尔值。如果 disabled 为 true，该选项（option）将会被选中
- [ ] react_learn_referencing-values-with-refs.md-11  —  其视为没有设置函数的常规 state 变量。 如果你熟悉面向对象编程，ref 可能会让你想起实例字段 —— 但是你写的不是 this.something，而是 somethingRef.current
- [ ] react_learn_referencing-values-with-refs.md-12  —  某些信息，请使用 state 代替。由于 React 不知道 ref.current 何时发生变化，即使在渲染时读取它也会使组件的行为难以预测。（唯一的例外是像 if (!ref.current) r
- [ ] react_learn_removing-effect-dependencies.md-14  —  ment 总是 1。为什么？因为定时器每秒调用 onTick 函数，实际运行的是 setCount(0 + 1)[1]，所以你总是看到 1。像这样的错误，当它们分散在多个组件中时，就更难解决了。 这里
- [ ] react_learn_render-and-commit.md-4  —  程中, React 将计算它们的哪些属性（如果有的话）自上次渲染以来已更改。在下一步（提交阶段）之前，它不会对这些信息执行任何操作。 ### 陷阱 渲染必须始终是一次 纯计算: - 输入相同，输出相同
- [ ] react_reference_react-dom_components_common.md-3  —  suppressHydrationWarning 为 true，React 不会在元素属性和内容不匹配时发出警告。它只能在同级工作，并被作为脱围机制。阅读有关抑制激活错误的内容。 style：CSS 
- [ ] react_reference_react-dom_components_style.md-2  —  同的样式表，并在样式表加载时 挂起。 请提供 href 和 precedence 属性以选择此行为。如果样式表具有相同的 href，React 将对样式去重。优先级属性告诉 React 在文档的 <h
- [ ] react_reference_react-dom_server_renderToPipeableStream.md-23  —  。 - 它将会“放弃”尝试在服务端渲染 Posts 组件的内容。 - 当 JavaScript 在客户端代码加载时，React 将会在客户端 重试 渲染 Posts 组件。 如果在客户端重试渲染 Po
- [ ] react_reference_react_useRef.md-1  —  urrent 属性的初始值。可以是任意类型的值。这个参数在首次渲染后被忽略。 #### 返回值 useRef 返回一个只有一个属性的对象: - current：初始值为传递的 initialValue

### 12. [语义改写] 当 option 元素没有显式指定 label 时，它的含义文字从哪里获取？

- [x] react_reference_react-dom_components_option.md-1  —  ops <option> 支持所有 常见的元素属性。 除此之外，<option> 还支持以下属性： - disabled：布尔值。如果 disabled 为 true，该选项（option）将会被选中
- [ ] react_learn_lifecycle-of-reactive-effects.md-23  —  音乐</option> </select> </label> <hr /> <ChatRoom roomId={roomId} /> </> ); } ``` 显示更多 无论何时更改一个类似 room
- [ ] react_learn_passing-data-deeply-with-context.md-10  —  Section> </Section> </Section> </Section> ); } ``` 显示更多 注意！这个示例还不能运行。所有 headings 的尺寸都一样，因为 即使你正在使用 c
- [ ] react_learn_sharing-state-between-components.md-14  —  {label} {' '} <input value={text} onChange={handleChange} /> </label> ); } ```
- [ ] react_reference_react-dom_components_select.md-1  —  elect> 支持所有 常见的元素属性。 你可以通过传递 value 属性 以控制选择框: - value：一个字符串（如果指定 multiple={true}，那么 value 也可以是一个字符串数
- [ ] react_reference_react_Fragment.md-11  —  渲染 Fragment 列表 在这种情况下，你需要显式地表示为 Fragment，而不是使用简写语法 <></>。当你在循环中渲染多个元素时，你需要为每一个元素分配一个 key。如果这个元素为 Fra
- [ ] vue_guide_best-practices_accessibility.md-4  —  e="complementary" | 用来支持主内容，同时其自身的内容是相对独立且有意义的 | | search | role="search" | 该章节包含整个应用的搜索功能 | | form 
- [ ] vue_guide_best-practices_accessibility.md-6  —  v-model="name" :aria-label="nameLabel" /> 在 Chrome DevTools 中审查此元素，查看无障碍名称是如何更改的： !Chrome 开发者工具正在通过 
- [ ] vue_guide_components_attrs.md-4  —  false 和使用 v-bind="$attrs" 来实现： vue-html{2} Click Me 小提示：没有参数的 v-bind 会将一个对象的所有属性都作为 attribute 应用到目标元

### 13. [概念术语] React 编译器要如何配置才能只对加了标记的函数进行编译，实现渐进式迁移？

- [x] react_reference_react-compiler_compilationMode.md-3  —  ## 使用注解模式进行增量采用 为了逐步迁移，可以使用 'annotation' 模式，仅编译被标记的函数： ``` { compilationMode: 'annotation'} ``` 然后显式
- [ ] react_learn_react-compiler.md-0  —  学习 React Copy pageCopy # React 编译器 ## 介绍 学习 React 编译器的作用 以及它如何通过自动处理记忆化（memoization）来优化你的 React 应用，从
- [ ] react_learn_react-compiler_incremental-adoption.md-0  —  学习 ReactReact Compiler Copy pageCopy # 逐步使用 React 编译器可以逐步采用，允许你首先在代码库的特定部分尝试使用。本指南将向你展示如何在现有项目中逐步推广该
- [ ] react_learn_react-compiler_incremental-adoption.md-1  —  何违反 React 规则的问题。你可以在扩展编译器覆盖范围的同时有条不紊地解决这些问题，而不是一次性修复整个代码库中的违规问题。这使迁移过程更易于管理，并降低了引入错误的风险。 通过控制代码中哪些部分
- [ ] react_learn_react-compiler_installation.md-9  —  器跳过对该特定组件的优化。你应该修复根本问题，并在解决后移除该指令。 如需更多故障排除帮助，请参阅调试指南。 ## 下一步 既然你已经安装了 React 编译器，可以进一步了解以下内容： - Reac
- [ ] react_learn_react-compiler_introduction.md-3  —  iveProcessing(data); const handleClick = (item) => { onClick(item.id); }; return ( <div> {processedD
- [ ] react_learn_react-compiler_introduction.md-9  —  的依赖项，即使其依赖项没有实质性变化，effect 也不会反复触发。 对于增量代码，我们建议依赖编译器进行记忆化，并在需要时使用 useMemo/useCallback 以实现精确控制。 对于现有代码
- [ ] react_reference_react-compiler_compiling-libraries.md-0  —  API 参考 Copy pageCopy # 编译库 本指南旨在帮助库作者理解如何使用 React 编译器来为用户提供经过优化的库代码。 - 为什么要发布编译后的代码？ - 设置编译 向下兼容性 - 
- [ ] react_reference_react-compiler_configuration.md-0  —  API 参考 Copy pageCopy # 配置 本页列出 React 编译器的所有可用配置项。 ### 注意 对于大多数应用，默认选项开箱即用即可满足需求。如果你有特殊需求，你可以使用这些高级选项
- [ ] react_reference_react-compiler_directives_use-memo.md-3  —  .} ``` #### 你正在渐进式地引入 React 编译器 可以从 annotation 模式开始，并有选择性地优化那些稳定的组件： ``` // 从优化叶子组件开始function Button

### 14. [命名精确] 当项目使用 Flow 类型系统而非 TypeScript 时，编译器的 compilationMode 应该设置成什么值？

- [x] react_reference_react-compiler_compilationMode.md-3  —  ## 使用注解模式进行增量采用 为了逐步迁移，可以使用 'annotation' 模式，仅编译被标记的函数： ``` { compilationMode: 'annotation'} ``` 然后显式
- [ ] react_reference_eslint-plugin-react-hooks_lints_config.md-0  —  API 参考Lints Copy pageCopy # config 验证编译器 配置选项。 ## 规则详情 React 编译器接受各种 配置选项 来控制其行为。此规则验证你的配置使用了正确的选项名称
- [ ] react_reference_react-compiler_compilationMode.md-0  —  API 参考配置 Copy pageCopy # compilationMode compilationMode 选项控制 React 编译器如何选择要编译的函数。 ``` { compilation
- [ ] react_reference_react-compiler_compilationMode.md-1  —  memo" 指令注释的函数 - 命名类似组件（PascalCase）或 Hook（use 前缀）并且创建了 JSX 和/或调用了其他 Hook 的函数 'annotation'：仅编译使用 "use 
- [ ] react_reference_react-compiler_panicThreshold.md-1  —  使用 'none' 时，编译器会自动检测并跳过有问题的代码 - 更高的阈值仅在开发调试时有用 ## 用法 ### 生产环境配置（推荐） 对于生产构建，始终使用 'none'。这是默认值： ``` { 
- [ ] react_reference_react_useDeferredValue.md-15  —  rt SlowList from './SlowList.js'; export default function App() { const [text, setText] = useState('
- [ ] vue_guide_typescript_overview.md-0  —  # 搭配 TypeScript 使用 Vue 像 TypeScript 这样的类型系统可以在编译时通过静态分析检测出很多常见错误。这减少了生产环境中的运行时错误，也让我们在重构大型项目的时候更有信心。
- [ ] vue_guide_typescript_overview.md-4  —  目中，你需要通过 compilerOptions.paths 选项为 TypeScript 再配置一遍。 * 如果你打算在 Vue 中使用 TSX，请将 compilerOptions.jsx 设置为

### 15. [概念术语] React 应用中，哪一类组件通常位于渲染树底部、没有子组件且会频繁重新渲染？

- [x] react_learn_understanding-your-ui-as-a-tree.md-4  —  ationGenerator'; import Copyright from './Copyright'; export default function App() { return ( <> <F
- [ ] react_learn_describing-the-ui.md-14  —  t function TeaSet() { return ( <> <Cup guest={1} /> <Cup guest={2} /> <Cup guest={3} /> </> ); } ```
- [ ] react_learn_understanding-your-ui-as-a-tree.md-1  —  用程序中流动以及如何优化呈现和应用程序大小。 ## 渲染树 组件的一个主要特性是能够由其他组件组合而成。在 嵌套组件 中有父组件和子组件的概念，其中每个父组件本身可能是另一个组件的子组件。 当渲染 R
- [ ] react_learn_understanding-your-ui-as-a-tree.md-2  —  tle text="Get Inspired App" /> <InspirationGenerator> <Copyright year={2004} /> </InspirationGenerat
- [ ] react_learn_understanding-your-ui-as-a-tree.md-5  —  染性能，通常包含最多复杂性。叶子组件位于树的底部，没有子组件，通常会频繁重新渲染。 识别这些组件类别有助于理解应用程序的数据流和性能。 ## 模块依赖树 在 React 应用程序中，可以使用树来建模的
- [ ] react_learn_understanding-your-ui-as-a-tree.md-7  —  。使用不同的属性值，组件可能会渲染不同的子组件。 - 渲染树有助于识别顶级组件和叶子组件。顶级组件会影响其下所有组件的渲染性能，而叶子组件通常会频繁重新渲染。识别它们有助于理解和调试渲染性能问题。 -
- [ ] react_reference_react_memo.md-21  —  xpensiveChild 的重新渲染 这意味着 在使用 React 编译器时，你可以放心移除 React.memo. 编译器会自动提供相同的优化，让代码更简洁更易维护。 ### 注意 编译器的优化实
- [ ] vue_guide_scaling-up_testing.md-3  —  ', () => { expect(increment(10)).toBe(10) }) }) 如前所述，单元测试通常适用于独立的业务逻辑、组件、类、模块或函数，不涉及 UI 渲染、网络请求或其他环境

### 16. [数字精确] 示例里 Copyright 组件接收的 year 属性值是多少？

- [x] react_learn_understanding-your-ui-as-a-tree.md-4  —  ationGenerator'; import Copyright from './Copyright'; export default function App() { return ( <> <F
- [ ] react_learn_understanding-your-ui-as-a-tree.md-2  —  tle text="Get Inspired App" /> <InspirationGenerator> <Copyright year={2004} /> </InspirationGenerat
- [ ] react_reference_react-dom_components_input.md-27  —  件在每次渲染时重新挂载），就会发生这种情况。 ### 收到错误：“A component is changing an uncontrolled input to be controlled” 提供的
- [ ] react_reference_react-dom_components_option.md-2  —  ption> 都设置一个 value 属性，表示要与表单一起提交的数据。 在这里了解更多关于 如何展示一个包含一系列 <option> 组件的 <select> 的信息。 ``` App.jsApp.
- [ ] react_reference_react-dom_components_select.md-2  —  utoFocus：布尔值。如果为 true，React 将在挂载时聚焦该元素。 - children：<select> 接受 <option>、<optgroup> 与 <datalist> 组件作为
- [ ] react_reference_react-dom_components_textarea.md-1  —  制文本框。 - value：一个字符串，用于控制文本框内的文本。 当你传递 value 时，你必须同时传递一个 onChange 处理函数，用于更新传递的值。 如果 <textarea> 是非受控组件
- [ ] react_reference_react-dom_components_textarea.md-16  —  错误：“A component is changing an uncontrolled input to be controlled” 提供的 value 属性必须在整个生命周期中都为字符串。 你不能
- [ ] react_reference_rsc_use-client.md-3  —  建了一个客户端模块的子树。 为了更好地说明这一点，请参考下面的 React 服务器组件应用程序示例。 ``` App.jsFancyText.jsInspirationGenerator.jsCopy
- [ ] react_reference_rsc_use-client.md-7  —  tor 包含 'use client' 指示符。 这意味着 FancyText 的组件定义将在服务器上进行评估，同时也将被客户端下载以渲染其客户端组件的使用。 深入探讨 #### 为什么 Copyri
- [ ] react_reference_rsc_use-client.md-8  —  这种情况下，InspirationGenerator 以 children 的形式接收 Copyright。然而，InspirationGenerator 模块从未直接导入 Copyright 模块，

### 17. [概念术语] 在响应式变量作为参数传入函数时，为什么会出现响应性丢失的情况？

- [x] vue_guide_extras_reactivity-transfor.md-5  —  ops: { msg: { type: String, required: true }, count: { type: Number, default: 1 }, foo: String }, se
- [ ] vue_api_composition-api-setup.md-1  —  } 在模板中访问从 setup 返回的 ref 时，它会自动浅层解包，因此你无须再在模板中为它写 .value。当通过 this 访问时也会同样如此解包。 setup() 自身并不含对组件实例的访问权
- [ ] vue_api_options-composition.md-1  —  turn { msg: 'foo' } } provide() { return { msg: this.msg } } } 请注意，针对上面这个例子，所供给的 msg 将不会是响应式的。请查看和响应
- [ ] vue_guide_essentials_reactivity-fundamentals.md-14  —  传递给函数时，我们将丢失响应性连接： js const state = reactive({ count: 0 }) // 当解构时，count 已经与 state.count 断开连接 let { 
- [ ] vue_guide_extras_reactivity-transfor.md-6  —  面的例子不会正常工作，因为代码被编译成了这样： ts let count = ref(0) trackChange(count.value) 这里的 count.value 是以一个 number 类
- [ ] vue_guide_extras_reactivity-transform.md-1  —  ，表明最终的 count 变量需要是一个响应式变量。 响应式的变量可以像普通变量那样被访问和重新赋值，但这些操作在编译后都会变为带 .value 的 ref。比如上面例子中 部分的代码就被编译成了下面
- [ ] vue_guide_extras_reactivity-transform.md-5  —  ops: { msg: { type: String, required: true }, count: { type: Number, default: 1 }, foo: String }, se
- [ ] vue_guide_extras_reactivity-transform.md-6  —  面的例子不会正常工作，因为代码被编译成了这样： ts let count = ref(0) trackChange(count.value) 这里的 count.value 是以一个 number 类

### 18. [数字精确] watchEffect 中打印的 props 的 count 属性默认值是多少？

- [x] vue_guide_extras_reactivity-transfor.md-5  —  ops: { msg: { type: String, required: true }, count: { type: Number, default: 1 }, foo: String }, se
- [ ] vue_api_options-state.md-4  —  quired 值为真值且 prop 未被传入，一个控制台警告将会被抛出。 * validator：将 prop 值及其对象作为参数传入的自定义验证函数。在开发模式下，如果该函数返回一个假值 (即验证失
- [ ] vue_api_sfc-script-setup.md-7  —  不支持需要实际类型分析的一些复杂类型，例如条件类型等。你可以在单个 prop 的类型上使用条件类型，但不能对整个 props 对象使用。 ### 响应式 Props 解构 在 Vue 3.5 及以上版
- [ ] vue_api_sfc-script-setup.md-8  —  }) 此外，你可以使用 JavaScript 原生的默认值语法声明 props 的默认值。这在使用基于类型的 props 声明时特别有用。 ts interface Props { msg?: str
- [ ] vue_guide_components_props.md-2  —  可使用 Number 构造函数作为其声明的值。 对象形式的 props 声明不仅可以一定程度上作为组件的文档，而且如果其他开发者在使用你的组件时传递了错误的类型，也会在浏览器控制台中抛出警告。我们将在
- [ ] vue_guide_extras_reactivity-in-dep.md-7  —  t A1 = ref(1) const A2 = ref() watchEffect(() => { // 追踪 A0 和 A1 A2.value = A0.value + A1.value }) /
- [ ] vue_guide_extras_reactivity-in-depth.md-7  —  t A1 = ref(1) const A2 = ref() watchEffect(() => { // 追踪 A0 和 A1 A2.value = A0.value + A1.value }) /
- [ ] vue_guide_extras_reactivity-transfor.md-4  —  的变量将不是响应式的、也不会更新。 2. 当使用基于类型的 props 的声明时，无法很方便地声明这些 prop 的默认值。为此我们提供了 withDefaults() 这个 API，但使用起来仍然很
- [ ] vue_guide_extras_reactivity-transform.md-4  —  的变量将不是响应式的、也不会更新。 2. 当使用基于类型的 props 的声明时，无法很方便地声明这些 prop 的默认值。为此我们提供了 withDefaults() 这个 API，但使用起来仍然很

### 19. [命名精确] React 中哪个 Hook 可以用来限制 ref 暴露给父组件的功能范围？

- [x] react_learn_manipulating-the-dom-with-refs.md-15  —  return ( <> <MyInput ref={inputRef} /> <button onClick={handleClick}> 聚焦输入框 </button> </> ); } ``` 显
- [ ] react_learn_state-a-components-memory.md-5  —  <img src={sculpture.url} alt={sculpture.alt} /> <p> {sculpture.description} </p> </> ); } ``` 显示更多 #
- [ ] react_learn_state-a-components-memory.md-30  —  age 组件“不知道”关于 Gallery state 的任何信息，甚至不知道它是否有任何 state。与 props 不同，state 完全私有于声明它的组件。父组件无法更改它。这使你可以向任何组件
- [ ] react_reference_react.md-2  —  达出来： - 组件与 Hook 必须是纯粹的 —— 组件与 Hook 的纯粹代码更易于理解、调试，并允许 React 自动优化组件与 Hook。 - React 调用组件与 Hook —— React
- [ ] react_reference_react_forwardRef.md-0  —  API 参考过时的 React API Copy pageCopy # forwardRef ### 已废弃 In React 19, forwardRef is no longer necessar
- [ ] react_reference_react_forwardRef.md-2  —  render 函数 forwardRef 接受一个渲染函数作为参数。React 将会使用 props 和 ref 调用此函数： ``` const MyInput = forwardRef(funct
- [ ] react_reference_react_forwardRef.md-3  —  性。 ## 用法 ### 将 DOM 节点暴露给父组件 默认情况下，每个组件的 DOM 节点都是私有的。然而，有时候将 DOM 节点公开给父组件是很有用的，比如允许对它进行聚焦。将组件定义包装在 fo
- [ ] react_reference_react_useImperativeHandle.md-0  —  API 参考Hook Copy pageCopy # useImperativeHandle useImperativeHandle 是 React 中的一个 Hook，它能让你自定义由 ref 暴露
- [ ] react_reference_rules.md-2  —  改它们。在创建 JSX 之前进行修改。 ## React 调用组件和 Hook React 负责在必要时渲染组件和 Hook 以优化用户体验。它是声明式的：你在组件逻辑中告诉 React 需要渲染什么
- [ ] react_reference_rules_react-calls-components-and-hooks.md-1  —  Article()}</Layout>; // 🔴 错误的：不要直接调用组件函数} ``` 如果组件包含 Hook，在循环或条件语句中直接调用它们时，很容易违反 Hook 的规则。 让 React 来

### 20. [语义改写] 在 React 里，如果不想让父组件通过 ref 完全访问子组件的 DOM 元素，应该采用什么方式？

- [x] react_learn_manipulating-the-dom-with-refs.md-15  —  return ( <> <MyInput ref={inputRef} /> <button onClick={handleClick}> 聚焦输入框 </button> </> ); } ``` 显
- [ ] react_learn_escape-hatches.md-0  —  学习 React Copy pageCopy # 脱围机制（Escape Hatches） 高级 有些组件可能需要控制和同步 React 之外的系统。例如，你可能需要使用浏览器 API 聚焦输入框，或
- [ ] react_learn_manipulating-the-dom-with-refs.md-8  —  用一个 ref 引用其父元素，然后用 DOM 操作方法如 querySelectorAll 来寻找它的子节点。然而，这种方法很脆弱，如果 DOM 结构发生变化，可能会失效或报错。 另一种解决方案是将函
- [ ] react_learn_manipulating-the-dom-with-refs.md-17  —  中的 realInputRef 保存了实际的 input DOM 节点。 但是，useImperativeHandle 指示 React 将你自己指定的对象作为父组件的 ref 值。 所以 Form 
- [ ] react_learn_manipulating-the-dom-with-refs.md-26  —  </div> ); } ``` 显示更多 在你手动删除 DOM 元素后，尝试使用 setState 再次显示它会导致崩溃。这是因为你更改了 DOM，而 React 不知道如何继续正确管理它。 避免更改
- [ ] react_learn_preserving-and-resetting-state.md-34  —  用户再次选择前一个收件人时恢复输入 state。对于一个不可见的组件，有几种方法可以让它的 state “活下去”： - 与其只渲染现在这一个聊天，你可以把 所有 聊天都渲染出来，但用 CSS 把其他
- [ ] react_reference_react-dom_createPortal.md-1  —  om';// ...<div> <p>这个子节点被放置在父节点 div 中。</p> {createPortal( <p>这个子节点被放置在 document body 中。</p>, documen
- [ ] react_reference_react_useImperativeHandle.md-2  —  对应的之前值。如果一次重新渲染导致某些依赖项发生了改变，或你没有提供这个参数列表，你的函数 createHandle 将会被重新执行，而新生成的句柄则会被分配给 ref。 ### 注意 从 React
- [ ] vue_api_built-in-special-attributes.md-1  —  触发。 * 参考指南 - 列表渲染 - 通过 key 管理状态 ## ref 用于注册模板引用。 * 预期：string | Function * 详细信息 ref 用于注册元素或子组件的引用。 使用
- [ ] vue_guide_essentials_template-refs.md-4  —  如果一个子组件使用的是选项式 API 或没有使用 ，被引用的组件实例和该子组件的 this 完全一致，这意味着父组件对子组件的每一个属性和方法都有完全的访问权。这使得在父组件和子组件之间创建紧密耦合的

### 21. [命名精确] 在 Messenger 组件里，哪个 state 变量用来记录当前选中的联系人？

- [x] react_learn_managing-state.md-12  —  会清空输入框。这可能会导致用户不小心发错消息： ``` App.jsContactList.jsChat.jsApp.jsReloadClearForkimport { useState } from
- [ ] react_learn_choosing-the-state-structure.md-1  —  e。如果你能在渲染期间从组件的 props 或其现有的 state 变量中计算出一些信息，则不应将这些信息放入该组件的 state 中。 - 避免重复的 state。当同一数据在多个 state 变量
- [ ] react_learn_choosing-the-state-structure.md-4  —  </div> ) } ``` 显示更多 另一种你需要将数据整合到一个对象或一个数组的情况是，你不知道未来需要多少个 state 片段。例如，有一个用户可以添加自定义字段的表单时，这将会很有帮助。 ##
- [ ] react_learn_choosing-the-state-structure.md-15  —  stName 时，你会触发一次重新渲染，然后下一个 fullName 将从新数据中计算出来。 深入探讨 #### 不要在 state 中镜像 props 显示更多 以下代码是体现 state 冗余的一
- [ ] react_learn_extracting-state-logic-into-a-reducer.md-27  —  fault function Messenger() { const [state, dispatch] = useReducer(messengerReducer, initialState); c
- [ ] react_learn_preserving-and-resetting-state.md-33  —  s[0]); return ( <div> <ContactList contacts={contacts} selectedContact={to} onSelect={contact => set
- [ ] react_learn_reacting-to-input-with-state.md-14  —  不代表任何你希望用户看到的有效 UI 的情况。（比如你绝对不会想要在展示错误信息的同时禁用掉输入框，导致用户无法纠正错误！） 这有一些你可以问自己的， 关于 state 变量的问题： - 这个 sta
- [ ] react_learn_state-a-components-memory.md-10  —  } ``` 显示更多 如果它们不相关，那么存在多个 state 变量是一个好主意，例如本例中的 index 和 showMore。但是，如果你发现经常同时更改两个 state 变量，那么最好将它们合并
- [ ] react_learn_state-a-components-memory.md-30  —  age 组件“不知道”关于 Gallery state 的任何信息，甚至不知道它是否有任何 state。与 props 不同，state 完全私有于声明它的组件。父组件无法更改它。这使你可以向任何组件
- [ ] react_reference_react_createElement.md-6  —  ); } export default function App() { return createElement( Greeting, { name: '泰勒' } ); } ``` 显示更多 这里

### 22. [语义改写] 当用户在联系人列表中点击某个联系人时，代码是如何把选中结果传递给 Chat 组件的？

- [x] react_learn_managing-state.md-12  —  会清空输入框。这可能会导致用户不小心发错消息： ``` App.jsContactList.jsChat.jsApp.jsReloadClearForkimport { useState } from
- [ ] react_learn_preserving-and-resetting-state.md-32  —  是！ 你不应该让用户因为一次偶然的点击而把他们已经输入的信息发送给一个错误的人。要修复这个问题，只需给组件添加一个 key ： ``` <Chat key={to.id} contact={to} /
- [ ] react_learn_reusing-logic-with-custom-hooks.md-31  —  </> ); } ``` 显示更多 注意你不再需要为了使用它而去了解 useChatRoom 是 如何 工作的。你可以把它添加到其他任意组件，传递其他任意选项，而它会以同样的方式工作。这就是自定义 H
- [ ] react_learn_synchronizing-with-effects.md-0  —  学习 React脱围机制 Copy pageCopy # 使用 Effect 进行同步 有些组件需要与外部系统同步。例如，你可能希望根据 React state 控制非 React 组件、建立服务器连
- [ ] react_learn_you-might-not-need-an-effect.md-1  —  数据。例如，你想在展示一个列表前先做筛选。你的直觉可能是写一个当列表变化时更新 state 变量的 Effect。然而，这是低效的。当你更新这个 state 时，React 首先会调用你的组件函数来计
- [ ] react_reference_react-dom_hooks_useFormStatus.md-5  —  t() { // ✅ `pending` 将从包裹 Submit 组件的表单派生 const { pending } = useFormStatus(); return <button disable
- [ ] react_reference_react_useCallback.md-26  —  Callback 函数，但是这不被允许 假设 Chart 组件被包裹在 memo 中。你希望在 ReportList 组件重新渲染时跳过重新渲染列表中的每个 Chart。但是，你不能在循环中调用 us
- [ ] react_reference_react_useDeferredValue.md-9  —  据加载后再次尝试重新渲染。用户将一直看到旧的延迟值，直到数据准备就绪。 被推迟的“后台”渲染是可中断的。例如，如果你再次在输入框中输入，React 将会中断渲染，并从新值开始重新渲染。React 总是
- [ ] react_reference_react_useRef.md-12  —  { return ( <input value={value} onChange={onChange} /> );} ``` 然后在组件的 props 参数中提取 ref，并将它作为参数传递给相关的 
- [ ] vue_guide_scaling-up_testing.md-20  —  expect(result.foo.value).toBe(1) // 如果需要的话可以这样触发 app.unmount() }) 对于更复杂的组合式函数，通过使用组件测试编写针对这个包装器组件的测试

### 23. [概念术语] 在 JSX 中，为什么不能直接返回多个并列的标签，而必须用父元素或 Fragment 包起来？

- [x] react_learn_writing-markup-with-jsx.md-5  —  点。 深入探讨 #### 为什么多个 JSX 标签需要被一个父元素包裹？ 显示更多 JSX 虽然看起来很像 HTML，但在底层其实被转化为了 JavaScript 对象，你不能在一个函数中返回多个对象
- [ ] react_learn_rendering-lists.md-10  —  { id: 4, // 在 JSX 中作为 key 使用 name: '苏布拉马尼扬·钱德拉塞卡', profession: '天体物理学家', accomplishment: '白矮星质量计算', 
- [ ] react_learn_tutorial-tic-tac-toe.md-13  —  utton>;} ``` 你将会得到如下错误： Console/src/App.js: Adjacent JSX elements must be wrapped in an enclosing ta
- [ ] react_learn_writing-markup-with-jsx.md-4  —  <div> 标签： ``` <div> <h1>海蒂·拉玛的待办事项</h1> <img src="https://react.dev/images/docs/scientists/yXOvdOSs.
- [ ] react_reference_react_Component.md-51  —  一般来说，你会让它返回一些 JSX。你的 render 方法应该是一个 纯函数：它应该只计算 JSX。 与 函数式组件 类似，类式组件可以从它的父组件 通过 props 接收信息。然而，读取 prop
- [ ] react_reference_react_createElement.md-6  —  ); } export default function App() { return createElement( Greeting, { name: '泰勒' } ); } ``` 显示更多 这里
- [ ] react_reference_react_Fragment.md-1  —  eraction - Canary only Tracking visibility with Fragment refs - Canary only Focus management with Fr
- [ ] react_reference_react_Fragment.md-7  —  ary only If you want to pass ref to a Fragment, you can’t use the <>...</> syntax. You have to expli

### 24. [语义改写] JSX 里像 img 这种没有子内容的标签，正确的书写格式是怎样的？

- [x] react_learn_writing-markup-with-jsx.md-5  —  点。 深入探讨 #### 为什么多个 JSX 标签需要被一个父元素包裹？ 显示更多 JSX 虽然看起来很像 HTML，但在底层其实被转化为了 JavaScript 对象，你不能在一个函数中返回多个对象
- [ ] react_learn_describing-the-ui.md-5  —  ent new traffic lights</li> <li>Rehearse a movie scene</li> <li>Improve spectrum technology</li> </u
- [ ] react_learn_writing-markup-with-jsx.md-0  —  学习 React描述 UI Copy pageCopy # 使用 JSX 书写标签语言 JSX 是 JavaScript 语法扩展，可以让你在 JavaScript 文件中书写类似 HTML 的标签。
- [ ] react_learn_writing-markup-with-jsx.md-7  —  dy Lamarr" className="photo"/> ``` 你可以 在 React DOM 元素中找到所有对应的属性。如果你在编写属性时发生了错误，不用担心 —— React 会在 浏览器控
- [ ] react_learn_your-first-component.md-3  —  eact.dev/images/docs/scientists/MK3eW3Am.jpg" alt="Katherine Johnson" /> ) } ``` 以下是构建组件的方法： ### 第一步
- [ ] react_reference_react-dom_components_common.md-43  —  TML 中的 class 属性： ``` <img className="avatar" /> ``` 然后你在单独的 CSS 文件中编写它的 CSS 规则： ``` /* 在你的 CSS 文件中 *
- [ ] react_reference_react-dom_components_title.md-1  —  OM 中唯一有效的位置，但如果表示特定页面的组件可以自行渲染其 <title>，这样做既方便又保持了可组合性。 有两个例外情况： - 如果 <title> 在 <svg> 组件内部，则没有特殊行为，因
- [ ] vue_guide_essentials_component-basics.md-12  —  比如 Tab 界面： 在演练场中查看示例 在演练场中查看示例 上面的例子是通过 Vue 的 元素和特殊的 is attribute 实现的： vue-html vue-html 在上面的例子中，被传给
- [ ] vue_guide_essentials_component-basics.md-13  —  ML 标签和属性名称是不分大小写的，所以浏览器会把任何大写的字符解释为小写。这意味着当你使用 DOM 内的模板时，无论是 PascalCase 形式的组件名称、camelCase 形式的 prop 名

### 25. [概念术语] 在 React 里，想让组件跨层级直接获取共享信息而不用一层层手动传参，应该怎么建立这种机制？

- [x] react_reference_react_createContext.md-4  —  函数的返回值渲染结果。当来自父组件的上下文发生变化时，React 会重新调用该函数。 ## 使用方法 ### 创建上下文 上下文使得组件能够无需通过显式传递参数的方式 将信息逐层传递。 在任何组件外调
- [ ] react_learn_escape-hatches.md-0  —  学习 React Copy pageCopy # 脱围机制（Escape Hatches） 高级 有些组件可能需要控制和同步 React 之外的系统。例如，你可能需要使用浏览器 API 聚焦输入框，或
- [ ] react_learn_passing-data-deeply-with-context.md-0  —  学习 React状态管理 Copy pageCopy # 使用 Context 深层传递参数 通常来说，你会通过 props 将信息从父组件传递到子组件。但是，如果你必须通过许多中间组件向下传递 pr
- [ ] react_learn_passing-data-deeply-with-context.md-1  —  p 逐级透传 要是有一种方法可以在组件树中不需要 props 将数据“直达”到所需的组件中，那可就太好了。React 的 context 功能可以满足我们的这个心愿。 ## Context：传递 pr
- [ ] react_learn_synchronizing-with-effects.md-33  —  卡中看到两条请求。这是正常的。使用上述方法，第一个 Effect 将立即被清理，所以它的 ignore 变量会被设置为 true。因此，即使有额外的请求，由于有 if (!ignore) 的检查，也不
- [ ] react_learn_synchronizing-with-effects.md-34  —  数据获取方式，特别是在完全客户端渲染的应用中。然而，这种方法非常手动化，并且有明显的弊端： - Effect 不会在服务端运行。这意味着最初由服务器渲染的 HTML 只会包含加载状态，而没有实际数据。
- [ ] react_learn_you-might-not-need-an-effect.md-0  —  学习 React脱围机制 Copy pageCopy # 你可能不需要 Effect Effect 是 React 范式中的一种脱围机制。它们让你可以 “逃出” React 并使组件和一些外部系统同步
- [ ] react_reference_rules_react-calls-components-and-hooks.md-1  —  Article()}</Layout>; // 🔴 错误的：不要直接调用组件函数} ``` 如果组件包含 Hook，在循环或条件语句中直接调用它们时，很容易违反 Hook 的规则。 让 React 来
- [ ] vue_guide_scaling-up_ssr.md-13  —  面访问，应用模块都会重新初始化。 然而，在 SSR 环境下，应用模块通常只在服务器启动时初始化一次。同一个应用模块会在多个服务器请求之间被复用，而我们的单例状态对象也一样。如果我们用单个用户特定的数据
- [ ] vue_guide_scaling-up_state-managemen.md-1  —  没有这么简单了： 1. 多个视图可能都依赖于同一份状态。 2. 来自不同视图的交互也可能需要更改同一份状态。 对于情景 1，一个可行的办法是将共享状态“提升”到共同的祖先组件上去，再通过 props 
- [ ] vue_guide_scaling-up_state-management.md-1  —  没有这么简单了： 1. 多个视图可能都依赖于同一份状态。 2. 来自不同视图的交互也可能需要更改同一份状态。 对于情景 1，一个可行的办法是将共享状态“提升”到共同的祖先组件上去，再通过 props 

### 26. [命名精确] React 中创建上下文需要调用哪个 API，它返回的是什么？

- [x] react_reference_react_createContext.md-4  —  函数的返回值渲染结果。当来自父组件的上下文发生变化时，React 会重新调用该函数。 ## 使用方法 ### 创建上下文 上下文使得组件能够无需通过显式传递参数的方式 将信息逐层传递。 在任何组件外调
- [ ] react_learn_state-a-components-memory.md-10  —  } ``` 显示更多 如果它们不相关，那么存在多个 state 变量是一个好主意，例如本例中的 index 和 showMore。但是，如果你发现经常同时更改两个 state 变量，那么最好将它们合并
- [ ] react_reference_react-dom_client_createRoot.md-1  —  t a DOM element” - 我得到了一个异常报错信息：“函数不是合法的 React 子项（Functions are not valid as a React child）” - 我的服务端
- [ ] react_reference_react-dom_components_common.md-26  —  v ref={(node) => { console.log('Attached', node); return () => { console.log('Clean up', node) }}}> 
- [ ] react_reference_react_cache.md-13  —  );async function DemoProfile() { // ✅ 正确示例：`getUser` 将进行记忆化。 const user = await getUser('demo-id'); 
- [ ] react_reference_react_createContext.md-0  —  API 参考API Copy pageCopy # createContext 使用 createContext 创建组件能够提供与读取的 上下文（context）。 ``` const SomeCo
- [ ] react_reference_react_createContext.md-5  —  ontext); // ...} ``` 默认情况下，它们将获得的值是你在创建上下文时指定的 默认值。然而，它本身并不是很有用，因为默认值永远不会发生改变。 上下文之所以有用，是因为可以 提供来自其他
- [ ] react_reference_react_createContext.md-6  —  发生变化， React 也会重新渲染读取该值的组件。 阅读更多有关读取和提供上下文的内容以及相关例子。 ### 从一个文件导入和导出上下文 通常，来自不同文件的组件都会需要读取同一个上下文。因此，在一
- [ ] react_reference_react_createElement.md-7  —  元素究竟是什么？ 显示更多 元素是用来描述一部分用户界面的轻量级结构。比如，<Greeting name="泰勒" /> 和 createElement(Greeting, { name: '泰勒' 

### 27. [概念术语] 如何让 MarkdownPreview 组件在真正需要渲染时才进行代码加载？

- [x] react_reference_react_lazy.md-3  —  ></Suspense> ``` 在这个例子中，MarkdownPreview 的代码只有在你尝试渲染它时才会被加载。如果 MarkdownPreview 还没有加载完成，将显示 Loading。请尝
- [ ] react_reference_react-dom_preload.md-3  —  的。 - 在浏览器中，可以在任何情况下调用 preload：例如渲染组件时、Effect 中以及事件处理程序中等等。 - 在服务器端渲染或渲染服务器组件时，只有在渲染组件时调用 preload 或在源
- [ ] react_reference_react-dom_preloadModule.md-3  —  仅仅是下载它），请改用 preinitModule；如果想加载一个不是 ESM 模块的脚本，请使用 preload。 ### 在事件处理程序中预加载 在转换到需要外部资源的页面或状态之前，于事件处理程
- [ ] react_reference_react_act.md-3  —  ed {count} times</p> <button onClick={handleClick}> Click me </button> </div> )} ``` ### 在测试中渲染组件 要测
- [ ] react_reference_react_lazy.md-0  —  API 参考API Copy pageCopy # lazy lazy 能够让你在组件第一次被渲染之前延迟加载组件的代码。 ``` const SomeComponent = lazy(load) `
- [ ] react_reference_react_lazy.md-2  —  常，你可以使用静态 import 声明来导入组件： ``` import MarkdownPreview from './MarkdownPreview.js'; ``` 如果想在组件第一次渲染前延迟
- [ ] react_reference_react_lazy.md-5  —  rkdown} /> </Suspense> )} </> ); } // 添加一个固定的延迟时间，以便你可以看到加载状态 function delayForDemo(promise) { retur
- [ ] vue_guide_best-practices_performance.md-4  —  下使用 Vue，并想要避免使用构建步骤，请考虑使用 petite-vue (只有 6kb) 来代替。 ### 代码分割 代码分割是指构建工具将构建后的 JavaScript 包拆分为多个较小的，可以按

### 28. [命名精确] 示例中通过哪个 React API 实现了组件的按需延迟加载？

- [x] react_reference_react_lazy.md-3  —  ></Suspense> ``` 在这个例子中，MarkdownPreview 的代码只有在你尝试渲染它时才会被加载。如果 MarkdownPreview 还没有加载完成，将显示 Loading。请尝
- [ ] react_learn_build-a-react-app-from-scratch.md-5  —  性获取页面的数据。 如果你从大多数后端或 REST 风格的 API 获取数据，我们建议使用： - TanStack Query - SWR - RTK Query 如果你从 GraphQL API 获
- [ ] react_learn_state-as-a-snapshot.md-10  —  Click 内部，number 的值即使在调用 setNumber(number + 5) 之后也还是 0。它的值在 React 通过调用你的组件“获取 UI 的快照”时就被“固定”了。 这里有个示例
- [ ] react_learn_synchronizing-with-effects.md-22  —  ，如果 ref 是从父组件传递过来的，则必须在依赖数组中指定它。这很有必要，因为你无法确定父组件是一直传递相同的 ref，还是根据条件传递不同的 ref。所以，你的 Effect 会依赖于被传递的是哪
- [ ] react_reference_react-dom_preload.md-4  —  reinit；如果想加载一个 ESM 模块，请使用 preloadModule。 下一个示例 ### 在事件处理程序中预加载 在转换到需要外部资源的页面或状态之前，于事件处理程序中调用 preload
- [ ] react_reference_react-dom_static_prerenderToNodeStream.md-5  —  nce 配合 CSP 来保护应用，那么在 prerender 的输出中包含该 nonce 值是不合适且不安全的。 ### 注意 ### 何时应使用 prerenderToNodeStream？ 静态的
- [ ] react_reference_react_Activity.md-11  —  且不会挂载它们的 Effect。 这种 预渲染 允许子组件提前加载所需的任何代码或数据。这样一来，当随后 Activity 边界变为可见时，子组件就能因为更短的加载时间从而更快的呈现出来。 让我们来看
- [ ] react_reference_react_apis.md-0  —  API 参考 Copy pageCopy # 内置的 React API 除了 Hooks 和 Components 之外，react 包还导出了一些其他的 API，这些 API 对于创建组件非常有用
- [ ] react_reference_react_lazy.md-0  —  API 参考API Copy pageCopy # lazy lazy 能够让你在组件第一次被渲染之前延迟加载组件的代码。 ``` const SomeComponent = lazy(load) `
- [ ] react_reference_react_lazy.md-2  —  常，你可以使用静态 import 声明来导入组件： ``` import MarkdownPreview from './MarkdownPreview.js'; ``` 如果想在组件第一次渲染前延迟
- [ ] vue_guide_components_async.md-3  —  会涉及到加载和错误状态，因此 defineAsyncComponent() 也支持在高级选项中处理这些状态： js const AsyncComp = defineAsyncComponent({ /

### 29. [命名精确] Vue 组件里用什么方式监听路由参数 id 的变化来触发数据重新获取？

- [x] vue_router_zh_guide_advanced_data-fetching.md-3  —  ss="loading">Loading...</div> <div v-if="error" class="error">{{ error }}</div> <div v-if="post" cla
- [ ] react_learn_build-a-react-app-from-scratch.md-4  —  不同部分。你还需要处理嵌套路由、路由参数和查询参数。路由可以在代码中配置，也可以根据组件文件夹和文件结构定义。 路由是现代应用程序的核心部分，通常与数据获取（包括为整个页面预取数据以加快加载速度）、代
- [ ] react_reference_react_Component.md-41  —  如果你需要运行副作用（例如，获取数据、运行动画或重新初始化监听）来响应 prop 或 state 的更改，请将该逻辑移至 componentDidUpdate。 - 如果需要从 DOM 中读取一些信息
- [ ] vue_guide_essentials_watchers.md-15  —  ost Watchers 如果想在侦听器回调中能访问被 Vue 更新之后的所属组件的 DOM，你需要指明 flush: 'post' 选项： js{6} export default { // ...
- [ ] vue_guide_scaling-up_routing.md-0  —  # 路由 ## 客户端 vs. 服务端路由 服务端路由指的是服务器根据用户访问的 URL 路径返回不同的响应结果。当我们在一个传统的服务端渲染的 web 应用中点击一个链接时，浏览器会从服务端获得全新
- [ ] vue_router_zh_guide_advanced_data-fetching.md-0  —  # 数据获取 ✨自信地编写 Vue 应用的 Vibe 代码RuleKit 有时候，进入某个路由后，需要从服务器获取数据。例如，在渲染用户信息时，你需要从服务器获取用户的数据。我们可以通过两种方式来实现
- [ ] vue_router_zh_guide_advanced_data-fetching.md-2  —  error = ref(null) // 侦听路由的参数，以便再次获取数据 watch(() => route.params.id, fetchData, { immediate: true }) a
- [ ] vue_router_zh_guide_advanced_data-fetching.md-4  —  te.params.id, this.fetchData, // 组件创建完后获取数据， // 此时 data 已经被监听了 { immediate: true } ) }, methods: { a
- [ ] vue_router_zh_guide_advanced_navigation-guards.md-0  —  # 导航守卫 在 Vue School 上观看免费视频课程✨自信地编写 Vue 应用的 Vibe 代码RuleKit 正如其名，vue-router 提供的导航守卫主要用来通过跳转或取消的方式守卫导航
- [ ] vue_router_zh_guide_essentials_dynamic-matching.md-2  —  API 参考中查看完整的细节。 这个例子的 demo 可以在这里找到。 ## 响应路由参数的变化 在 Vue School 上观看免费视频课程 使用带有参数的路由时需要注意的是，当用户从 /users

### 30. [语义改写] 这个组件在初始状态下把 loading、post 和 error 分别设为了什么值？

- [x] vue_router_zh_guide_advanced_data-fetching.md-3  —  ss="loading">Loading...</div> <div v-if="error" class="error">{{ error }}</div> <div v-if="post" cla
- [ ] react_learn_adding-interactivity.md-6  —  ） - 渲染组件（在厨房准备订单） - 提交到 DOM（将订单送到桌前） - Trigger - Render - Commit Rachel Lee Nabors 绘图 ## 想要仔细学习这个主题的
- [ ] react_learn_separating-events-from-effects.md-28  —  不会再发出警告。在稍早之前的示例中，你将 url 添加为依赖项，是因为 React 提醒你去做这件事。如果禁用代码检查，你未来将不会再收到任何关于 Effect 修改的提醒。这引起了 bug。 这个示
- [ ] react_reference_react-dom_server_renderToPipeableStream.md-23  —  。 - 它将会“放弃”尝试在服务端渲染 Posts 组件的内容。 - 当 JavaScript 在客户端代码加载时，React 将会在客户端 重试 渲染 Posts 组件。 如果在客户端重试渲染 Po
- [ ] react_reference_react-dom_server_renderToReadableStream.md-24  —  spense> 边界内）抛出错误，React 将不会停止渲染。这意味着会触发 onError 回调，但你的代码会继续运行，不会进入 catch 块。这是因为 React 将尝试从客户端的错误中恢复，就
- [ ] react_reference_react_createContext.md-5  —  ontext); // ...} ``` 默认情况下，它们将获得的值是你在创建上下文时指定的 默认值。然而，它本身并不是很有用，因为默认值永远不会发生改变。 上下文之所以有用，是因为可以 提供来自其他
- [ ] react_reference_react_useTransition.md-34  —  avedQuantity); }); }); }; return ( <div> <h1>Checkout</h1> <Item action={updateQuantityAction}/> <hr
- [ ] vue_router_zh_guide_advanced_data-fetching.md-1  —  <div v-if="loading" class="loading">Loading...</div> <div v-if="error" class="error">{{ error }}</di
- [ ] vue_router_zh_guide_advanced_data-fetching.md-2  —  error = ref(null) // 侦听路由的参数，以便再次获取数据 watch(() => route.params.id, fetchData, { immediate: true }) a
- [ ] vue_router_zh_guide_advanced_data-fetching.md-4  —  te.params.id, this.fetchData, // 组件创建完后获取数据， // 此时 data 已经被监听了 { immediate: true } ) }, methods: { a

### 31. [概念术语] React 的严格模式在开发时对组件函数会做什么特殊处理？

- [x] react_learn_keeping-components-pure.md-6  —  时，你应该 设置状态，而不是直接写入变量。当你的组件正在渲染时，你永远不应该改变预先存在的变量或对象。 React 提供了 “严格模式”，在严格模式下开发时，它将会调用每个组件函数两次。通过重复调用组
- [ ] react_learn_synchronizing-with-effects.md-0  —  学习 React脱围机制 Copy pageCopy # 使用 Effect 进行同步 有些组件需要与外部系统同步。例如，你可能希望根据 React state 控制非 React 组件、建立服务器连
- [ ] react_learn_synchronizing-with-effects.md-27  —  理的 Effect。你可以通过关闭 严格模式 来禁用这个行为，但我们建议保留它。它可以帮助你发现许多类似上述的 bug。 ## 如何处理在开发环境下 Effect 运行了两次？ React 有意在开发
- [ ] react_reference_react_StrictMode.md-2  —  de> 下移到树的较低层级。 ## 用法 ### 为整个应用启用严格模式 严格模式为 <StrictMode> 组件内的整个组件树启用额外的开发环境检查，这些检查有助于在开发过程中尽早地发现组件中的常
- [ ] react_reference_react_StrictMode.md-3  —  ，但它们有助于找出已经存在于代码中但在生产环境中可能难以复现的错误。严格模式让你在用户反馈之前就可以修复这些错误。 ### 注意 严格模式启用了以下仅在开发环境下有效的行为： - 组件将 重新渲染一次
- [ ] react_reference_react_StrictMode.md-5  —  cts to double fire without the parent effects, which cannot happen in production. ### 修复在开发过程中通过双重渲染
- [ ] react_reference_react_StrictMode.md-12  —  </li> ))} </ul> ); } ``` 显示更多 在没有严格模式的情况下，在你添加了更多的重新渲染前很容易忽视这个错误。而严格模式立即显示了相同的错误。严格模式可以帮助你在将错误推送给团队和

### 32. [语义改写] 如何启用 React 的严格模式，且它在生产环境中是否会影响性能？

- [x] react_learn_keeping-components-pure.md-6  —  时，你应该 设置状态，而不是直接写入变量。当你的组件正在渲染时，你永远不应该改变预先存在的变量或对象。 React 提供了 “严格模式”，在严格模式下开发时，它将会调用每个组件函数两次。通过重复调用组
- [ ] react_learn_render-and-commit.md-4  —  程中, React 将计算它们的哪些属性（如果有的话）自上次渲染以来已更改。在下一步（提交阶段）之前，它不会对这些信息执行任何操作。 ### 陷阱 渲染必须始终是一次 纯计算: - 输入相同，输出相同
- [ ] react_learn_synchronizing-with-effects.md-27  —  理的 Effect。你可以通过关闭 严格模式 来禁用这个行为，但我们建议保留它。它可以帮助你发现许多类似上述的 bug。 ## 如何处理在开发环境下 Effect 运行了两次？ React 有意在开发
- [ ] react_learn_synchronizing-with-effects.md-36  —  看，logVisit 不应该在开发环境中执行任何操作，因为你不会想让开发设备的日志影响生产环境的统计数据。每次保存文件时组件都会重新挂载，因此在开发环境中会记录额外的访问日志。 在生产环境中，不会有重
- [ ] react_reference_react_Profiler.md-3  —  r={onRender}> <Sidebar /> </Profiler> <PageContent /></App> ``` 这需要两个属性：id（字符串）和 onRender 回调函数（函数），每
- [ ] react_reference_react_StrictMode.md-2  —  de> 下移到树的较低层级。 ## 用法 ### 为整个应用启用严格模式 严格模式为 <StrictMode> 组件内的整个组件树启用额外的开发环境检查，这些检查有助于在开发过程中尽早地发现组件中的常
- [ ] react_reference_react_StrictMode.md-3  —  ，但它们有助于找出已经存在于代码中但在生产环境中可能难以复现的错误。严格模式让你在用户反馈之前就可以修复这些错误。 ### 注意 严格模式启用了以下仅在开发环境下有效的行为： - 组件将 重新渲染一次
- [ ] react_reference_react_StrictMode.md-12  —  </li> ))} </ul> ); } ``` 显示更多 在没有严格模式的情况下，在你添加了更多的重新渲染前很容易忽视这个错误。而严格模式立即显示了相同的错误。严格模式可以帮助你在将错误推送给团队和

### 33. [语义改写] 在 React 中，什么情况下才需要显式导入 Fragment 而不是使用简写语法？

- [x] react_reference_react_Fragment.md-9  —  ); } function PostTitle({ title }) { return <h1>{title}</h1> } function PostBody({ body }) { return 
- [ ] react_learn_rendering-lists.md-10  —  { id: 4, // 在 JSX 中作为 key 使用 name: '苏布拉马尼扬·钱德拉塞卡', profession: '天体物理学家', accomplishment: '白矮星质量计算', 
- [ ] react_learn_reusing-logic-with-custom-hooks.md-55  —  取的代码 变成 “外部系统”。这会让你的 Effect 保持简洁，因为他们只需要向已经被你移动到 React 外部的系统发送消息。 上面这个示例假设需要使用 JavaScript 写 fade-in 
- [ ] react_reference_react_Fragment.md-1  —  eraction - Canary only Tracking visibility with Fragment refs - Canary only Focus management with Fr
- [ ] react_reference_react_Fragment.md-10  —  元素分配给变量，作为 props 传递等： ``` function CloseDialog() { const buttons = ( <> <OKButton /> <CancelButton /
- [ ] react_reference_react_Fragment.md-11  —  渲染 Fragment 列表 在这种情况下，你需要显式地表示为 Fragment，而不是使用简写语法 <></>。当你在循环中渲染多个元素时，你需要为每一个元素分配一个 key。如果这个元素为 Fra
- [ ] react_reference_react_memo.md-3  —  >Hello, {name}!</h1>;});export default Greeting; ``` React 组件应该始终具有 纯粹的渲染逻辑。这意味着如果其 props、state 和 co

### 34. [命名精确] 示例中从 React 导入的 Fragment 是通过哪个导入语句实现的？

- [x] react_reference_react_Fragment.md-9  —  ); } function PostTitle({ title }) { return <h1>{title}</h1> } function PostBody({ body }) { return 
- [ ] react_learn_describing-the-ui.md-2  —  吗？ 请参阅 你的第一个组件 以学习如何声明并使用 React 组件 阅读更多 ## 组件的导入与导出 你可以在一个文件中声明许多组件，但文件的体积过大会变得难以浏览。为了解决这个问题，你可以在一个文
- [ ] react_learn_importing-and-exporting-components.md-0  —  学习 React描述 UI Copy pageCopy # 组件的导入与导出 组件的神奇之处在于它们的可重用性：你可以创建一个由其他组件构成的组件。但当你嵌套了越来越多的组件时，则需要将它们拆分成不同
- [ ] react_learn_importing-and-exporting-components.md-3  —  从 Gallery.js 中导入 Gallery 组件。 - 使用 默认导出 的方式，将根组件 App 导出。 ### 注意 引入过程中，你可能会遇到一些文件并未添加 .js 文件后缀，如下所示： `
- [ ] react_learn_importing-and-exporting-components.md-7  —  ，将 Gallery 组件导出。 App.js: - 使用 具名导入 的方式，从 Gallery.js 中导入 Profile 组件，并取名为 Profile。 - 使用 默认导入 的方式，从 Gal
- [ ] react_learn_thinking-in-react.md-10  —  来实现。 现在考虑示例应用程序中的每一条数据: - 产品原始列表 - 搜索用户键入的文本 - 复选框的值 - 过滤后的产品列表 其中哪些是 state 呢？标记出那些不是的: - 随着时间推移 保持不
- [ ] react_reference_react_Fragment.md-6  —  OM children with an IntersectionObserver or ResizeObserver. - unobserveUsing(observer): Stops observ
- [ ] react_reference_react_Fragment.md-7  —  ary only If you want to pass ref to a Fragment, you can’t use the <>...</> syntax. You have to expli
- [ ] react_reference_react_Fragment.md-11  —  渲染 Fragment 列表 在这种情况下，你需要显式地表示为 Fragment，而不是使用简写语法 <></>。当你在循环中渲染多个元素时，你需要为每一个元素分配一个 key。如果这个元素为 Fra

### 35. [命名精确] 在开发环境下，Vue 组件调试钩子接收到的调试事件对象里，type 字段可以取哪些值？

- [x] vue_guide_extras_reactivity-in-dep.md-11  —  ugger }, renderTriggered(event) { debugger } } 组件调试钩子仅会在开发模式下工作 调试事件对象有如下的类型定义： ts type DebuggerEven
- [ ] react_learn_synchronizing-with-effects.md-36  —  看，logVisit 不应该在开发环境中执行任何操作，因为你不会想让开发设备的日志影响生产环境的统计数据。每次保存文件时组件都会重新挂载，因此在开发环境中会记录额外的访问日志。 在生产环境中，不会有重
- [ ] react_reference_react_Component.md-9  —  rror 的实例，但是这并不能保证，因为 JavaScript 允许 抛出 所有值，包括字符串甚至是 null。 info：一个包含有关错误的附加信息的对象。它的 componentStack 字段包
- [ ] vue_api_composition-api-lifecycle.md-7  —  ptured 钩子或 app.config.errorHandler 因这个错误而被调用。 ## onRenderTracked() 注册一个调试钩子，当组件渲染过程中追踪到响应式依赖时调用。 这个钩
- [ ] vue_guide_extras_reactivity-in-dep.md-12  —  项的变更触发时被调用。 这两个回调都会作为组件调试的钩子，接受相同格式的调试事件： js const plusOne = computed(() => count.value + 1, { onTra
- [ ] vue_guide_extras_reactivity-in-depth.md-11  —  ugger }, renderTriggered(event) { debugger } } 组件调试钩子仅会在开发模式下工作 调试事件对象有如下的类型定义： ts type DebuggerEven
- [ ] vue_guide_extras_reactivity-in-depth.md-12  —  项的变更触发时被调用。 这两个回调都会作为组件调试的钩子，接受相同格式的调试事件： js const plusOne = computed(() => count.value + 1, { onTra
- [ ] vue_guide_scaling-up_testing.md-5  —  单元测试之上，可以被认为是集成测试的一种形式。你的 Vue 应用中大部分内容都应该由组件测试来覆盖，我们建议每个 Vue 组件都应有自己的组件测试文件。 组件测试应该捕捉组件中的 prop、事件、提供

### 36. [语义改写] 调用 computed() 时传入的第二个参数对象中，onTrack 和 onTrigger 分别在什么时机被触发？

- [x] vue_guide_extras_reactivity-in-dep.md-11  —  ugger }, renderTriggered(event) { debugger } } 组件调试钩子仅会在开发模式下工作 调试事件对象有如下的类型定义： ts type DebuggerEven
- [ ] react_reference_react-dom_components_common.md-7  —  uxClickCapture：一个在 捕获阶段 触发的 onAuxClick 版本。 - onBeforeInput：一个 InputEvent 触发。在可编辑元素的值被修改之前触发。React 尚未
- [ ] vue_api_reactivity-core.md-13  —  执行回调函数。 第一个参数是侦听器的源。这个来源可以是以下几种： * 一个函数，返回一个值 * 一个 ref * 一个响应式对象 * ...或是由以上类型的值组成的数组 第二个参数是在发生变化时要调用
- [ ] vue_guide_extras_reactivity-in-dep.md-12  —  项的变更触发时被调用。 这两个回调都会作为组件调试的钩子，接受相同格式的调试事件： js const plusOne = computed(() => count.value + 1, { onTra
- [ ] vue_guide_extras_reactivity-in-depth.md-11  —  ugger }, renderTriggered(event) { debugger } } 组件调试钩子仅会在开发模式下工作 调试事件对象有如下的类型定义： ts type DebuggerEven
- [ ] vue_guide_extras_reactivity-in-depth.md-12  —  项的变更触发时被调用。 这两个回调都会作为组件调试的钩子，接受相同格式的调试事件： js const plusOne = computed(() => count.value + 1, { onTra

### 37. [概念术语] 在 React 中，createElement 的第三个及后续参数代表什么？它们是否必须提供？

- [x] react_reference_react_createElement.md-4  —  dren： ``` import { createElement } from 'react';function Greeting({ name }) { return createElement( 
- [ ] react_learn_reacting-to-input-with-state.md-14  —  不代表任何你希望用户看到的有效 UI 的情况。（比如你绝对不会想要在展示错误信息的同时禁用掉输入框，导致用户无法纠正错误！） 这有一些你可以问自己的， 关于 state 变量的问题： - 这个 sta
- [ ] react_reference_react_Children.md-12  —  ); } function MoreRows() { return ( <> <p>这是第二项。</p> <p>这是第三项。</p> </> ); } ``` 显示更多 当操作 children 时，
- [ ] react_reference_react_createElement.md-0  —  API 参考过时的 React API Copy pageCopy # createElement createElement 允许你创建一个 React 元素。它可以作为 JSX 的替代方案。 ``
- [ ] react_reference_react_createElement.md-2  —  ll、undefined、true 和 false），以及 React 节点数组。 #### 返回值 createElement 返回一个 React 元素，它有这些属性： - type：你传入的 t
- [ ] react_reference_react_createElement.md-3  —  ething)，但 <something />（小写）等价于 createElement('something')（注意它是一个字符串，它会被当作内置的 HTML 标签）。 你应该仅 在所有子元素都是
- [ ] react_reference_react_useImperativeHandle.md-1  —  f }) { useImperativeHandle(ref, () => { return { // ... 你的方法 ... }; }, []); // ... ``` 请看下面的更多例子 ###
- [ ] react_reference_react_useImperativeHandle.md-2  —  对应的之前值。如果一次重新渲染导致某些依赖项发生了改变，或你没有提供这个参数列表，你的函数 createHandle 将会被重新执行，而新生成的句柄则会被分配给 ref。 ### 注意 从 React
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-0  —  API 参考概述 Copy pageCopy # 组件和 Hook 必须是纯粹的 纯函数仅仅执行计算，除此之外不做任何事情。这使得你的代码更易于理解和调试，并允许 React 能够正确地自动优化你的组
- [ ] vue_guide_components_provide-injec.md-11  —  fault { provide() { return { [myInjectionKey]: { /* 要提供的数据 */ } } } } js // 注入方组件 import { myInjecti

### 38. [语义改写] 如果想用 createElement 渲染自定义的 React 组件而不是像 'h1' 这样的原生标签，type 参数应该传什么？

- [x] react_reference_react_createElement.md-4  —  dren： ``` import { createElement } from 'react';function Greeting({ name }) { return createElement( 
- [ ] react_learn_describing-the-ui.md-9  —  想要仔细学习这个主题的内容吗？ 请参阅 将 Props 传递给组件 以了解如何传递并读取 props。 阅读更多 ## 条件渲染 你的组件经常需要根据不同的条件来显示不同的东西。在 React 中，你
- [ ] react_reference_react-dom_components_title.md-0  —  API 参考组件 Copy pageCopy # <title> 浏览器内置的 <title> 组件 允许向文档指定标题。 ``` <title>我的博客</title> ``` 参考 - <titl
- [ ] react_reference_react-dom_server_renderToReadableStream.md-2  —  更多示例。 #### 参数 reactNode：要渲染为 HTML 的 React 节点。例如，类似 <App /> 的 JSX 元素。它应该表示整个文档，因此 App 组件应该渲染 <html> 标
- [ ] react_reference_react_createElement.md-0  —  API 参考过时的 React API Copy pageCopy # createElement createElement 允许你创建一个 React 元素。它可以作为 JSX 的替代方案。 ``
- [ ] react_reference_react_createElement.md-2  —  ll、undefined、true 和 false），以及 React 节点数组。 #### 返回值 createElement 返回一个 React 元素，它有这些属性： - type：你传入的 t
- [ ] react_reference_react_createElement.md-3  —  ething)，但 <something />（小写）等价于 createElement('something')（注意它是一个字符串，它会被当作内置的 HTML 标签）。 你应该仅 在所有子元素都是
- [ ] react_reference_react_createElement.md-7  —  元素究竟是什么？ 显示更多 元素是用来描述一部分用户界面的轻量级结构。比如，<Greeting name="泰勒" /> 和 createElement(Greeting, { name: '泰勒' 
- [ ] react_reference_react_isValidElement.md-4  —  果你调用另外一个 API，它 只 接受元素（像 cloneElement 那样），并且你想在参数不是 React 元素时避免报错，则这个方法是最有用的。 除非你有某些特定的原因需要添加 isValid

### 39. [命名精确] 这段代码里，当访问的路径在路由表中找不到对应组件时，会默认渲染哪个组件？

- [x] vue_guide_scaling-up_routing.md-2  —  return routes[currentPath.value.slice(1) || '/'] || NotFound }) Home | About | Broken Link 在演练场中尝试一下
- [ ] react_learn_state-a-components-memory.md-10  —  } ``` 显示更多 如果它们不相关，那么存在多个 state 变量是一个好主意，例如本例中的 index 和 showMore。但是，如果你发现经常同时更改两个 state 变量，那么最好将它们合并
- [ ] react_learn_thinking-in-react.md-12  —  eact 使用单向数据流，通过组件层级结构从父组件传递数据至子组件。要搞清楚哪个组件拥有哪个 state。如果你是第一次阅读此章节，可能会很有挑战，但可以通过下面的步骤搞定它! 为你应用程序中的每一个
- [ ] react_reference_react-compiler_compiling-libraries.md-0  —  API 参考 Copy pageCopy # 编译库 本指南旨在帮助库作者理解如何使用 React 编译器来为用户提供经过优化的库代码。 - 为什么要发布编译后的代码？ - 设置编译 向下兼容性 - 
- [ ] vue_api_options-misc.md-1  —  或以上的版本中，使用 的单文件组件会自动根据文件名生成对应的 name 选项，即使是在配合 使用时也无需再手动声明。 ## inheritAttrs 用于控制是否启用默认的组件 attribute 透
- [ ] vue_router_zh_guide_advanced_data-fetching.md-6  —  }, // 路由改变前，组件就已经渲染完了 // 逻辑稍稍不同 async beforeRouteUpdate(to, from) { this.post = null getPost(to.para
- [ ] vue_router_zh_guide_advanced_router-view-slot.md-3  —  /> </router-view> ``` 而如果我们将引用放在 <router-view> 上，那引用将会被 RouterView 的实例填充，而不是路由组件本身。
- [ ] vue_router_zh_guide_essentials_dynamic-matching.md-0  —  # 带参数的动态路由匹配 在 Vue School 上观看免费视频课程 很多时候，我们需要将给定匹配模式的路由映射到同一个组件。例如，我们可能有一个 User 组件，它应该对所有用户进行渲染，但用户 
- [ ] vue_router_zh_guide_essentials_nested-routes.md-2  —  层的 router-view。它渲染顶层路由匹配的组件。同样地，一个被渲染的组件也可以包含自己嵌套的 <router-view>。例如，如果我们在 User 组件的模板内添加一个 <router-vi
- [ ] vue_router_zh_guide_essentials_nested-routes.md-4  —  想在那里渲染一些东西。在这种情况下，你可以提供一个空的嵌套路径： ``` jsconst routes = [ { path: '/user/:id', component: User, childr
- [ ] vue_router_zh_guide_essentials_redirect-and-alias.md-2  —  edirect: to => { // 该函数接收目标路由作为参数 return to.path.replace(/posts$/, 'profile') }, }, ] ``` ## 别名 重定向是

### 40. [概念术语] 这个简易路由实现是通过监听浏览器的哪个事件来感知 URL 变化的？

- [x] vue_guide_scaling-up_routing.md-2  —  return routes[currentPath.value.slice(1) || '/'] || NotFound }) Home | About | Broken Link 在演练场中尝试一下
- [ ] react_learn_you-might-not-need-an-effect.md-34  —  踪组件树来寻找错误信息是从哪个组件传递下来的，从而找到传递了错误的 prop 或具有错误的 state 的组件。当子组件在 Effect 中更新其父组件的 state 时，数据流变得非常难以追踪。既然
- [ ] vue_guide_scaling-up_routing.md-0  —  # 路由 ## 客户端 vs. 服务端路由 服务端路由指的是服务器根据用户访问的 URL 路径返回不同的响应结果。当我们在一个传统的服务端渲染的 web 应用中点击一个链接时，浏览器会从服务端获得全新
- [ ] vue_guide_scaling-up_routing.md-1  —  简单的页面路由，而不想为此引入一整个路由库，你可以通过动态组件的方式，监听浏览器 hashchange 事件或使用 History API 来更新当前组件。 下面是一个简单的例子： vue impor
- [ ] vue_router_zh_guide_advanced_data-fetching.md-6  —  }, // 路由改变前，组件就已经渲染完了 // 逻辑稍稍不同 async beforeRouteUpdate(to, from) { this.post = null getPost(to.para
- [ ] vue_router_zh_guide_advanced_router-view-slot.md-3  —  /> </router-view> ``` 而如果我们将引用放在 <router-view> 上，那引用将会被 RouterView 的实例填充，而不是路由组件本身。
- [ ] vue_router_zh_guide_essentials_dynamic-matching.md-2  —  API 参考中查看完整的细节。 这个例子的 demo 可以在这里找到。 ## 响应路由参数的变化 在 Vue School 上观看免费视频课程 使用带有参数的路由时需要注意的是，当用户从 /users
- [ ] vue_router_zh_guide_essentials_history-mode.md-9  —  *)', component: NotFoundComponent }], }) ``` 另外，如果你使用的是 Node.js 服务器，你可以通过在服务器端使用路由器来匹配传入的 URL，如果没有匹配
- [ ] vue_router_zh_guide_essentials_navigation.md-0  —  # 编程式导航 在 Vue School 上观看免费视频课程 除了使用 <router-link> 创建 a 标签来定义导航链接，我们还可以借助 router 的实例方法，通过编写代码来实现。 ## 

### 41. [概念术语] React 组件要满足什么条件才能被认为是幂等的？

- [x] react_reference_rules.md-1  —  插件 来帮助你的代码库遵循 React 规则。通过遵循 React 规则，你将能够发现并解决这些 bugs，并保持你的应用程序易于维护。 ## 组件和 Hook 必须是纯净的 组件和 Hook 中的纯
- [ ] react_learn_describing-the-ui.md-0  —  学习 React Copy pageCopy # 描述 UI React 是一个用于构建用户界面（UI）的 JavaScript 库，用户界面由按钮、文本和图像等小单元内容构建而成。React 帮助你
- [ ] react_learn_keeping-components-pure.md-9  —  事件处理程序无需是纯函数。 如果你用尽一切办法，仍无法为副作用找到合适的事件处理程序，你还可以调用组件中的 useEffect 方法将其附加到返回的 JSX 中。这会告诉 React 在渲染结束后执行
- [ ] react_learn_synchronizing-with-effects.md-21  —  aying]); ``` 这是因为 ref 具有 稳定 的标识：React 确保你在 每轮渲染中调用同一个 useRef 时，总能获得相同的对象。ref 不会改变，所以它不会导致重新运行 Effect
- [ ] react_learn_understanding-your-ui-as-a-tree.md-0  —  学习 React描述 UI Copy pageCopy # 将 UI 视为树 当 React 应用程序逐渐成形时，许多组件会出现嵌套。那么 React 是如何跟踪应用程序组件结构的？ React 以及
- [ ] react_learn_your-first-component.md-8  —  ✅ 在顶层声明组件function Profile() { // ...} ``` 当子组件需要使用父组件的数据时，你需要 通过 props 的形式进行传递，而不是嵌套定义。 深入探讨 #### 万物
- [ ] react_reference_react-dom_components_link.md-4  —  哪个位置被渲染，React 都会始终将其对应的 DOM 元素放在文档的 <head> 中。<head> 是 <link> 在 DOM 中唯一有效的位置，但如果表示特定页面的组件可以自行渲染 <link
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-0  —  API 参考概述 Copy pageCopy # 组件和 Hook 必须是纯粹的 纯函数仅仅执行计算，除此之外不做任何事情。这使得你的代码更易于理解和调试，并允许 React 能够正确地自动优化你的组
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-4  —  件和 Hook 必须是幂等的 组件必须始终根据其输入（props、state、和 context）返回相同的输出。这被称为“幂等性”。幂等性 是函数式编程中经常使用的一个术语，它指的是只要你使用相同的
- [ ] vue_router_zh_guide_essentials_active-links.md-0  —  # 匹配当前路由的链接 应用程序通常都会有一个渲染 RouterLink 列表的导航组件。我们也许想对这个列表中匹配当前路由的链接进行视觉区分。 RouterLink 组件会为匹配当前路由的链接添加两

### 42. [语义改写] 为什么副作用不应该在渲染过程中执行？

- [x] react_reference_rules.md-1  —  插件 来帮助你的代码库遵循 React 规则。通过遵循 React 规则，你将能够发现并解决这些 bugs，并保持你的应用程序易于维护。 ## 组件和 Hook 必须是纯净的 组件和 Hook 中的纯
- [ ] react_learn_keeping-components-pure.md-8  —  ; } return cups; } ``` 如果 cups 变量或 [] 数组是在 TeaGathering 函数之外创建的，这将是一个很大的问题！因为如果那样的话，当你调用数组的 push 方法时
- [ ] react_learn_responding-to-events.md-19  —  含副作用吗？ 当然可以！事件处理函数是执行副作用的最佳位置。 与渲染函数不同，事件处理函数不需要是 纯函数，因此它是用来 更改 某些值的绝佳位置。例如，更改输入框的值以响应键入，或者更改列表以响应按钮
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-0  —  API 参考概述 Copy pageCopy # 组件和 Hook 必须是纯粹的 纯函数仅仅执行计算，除此之外不做任何事情。这使得你的代码更易于理解和调试，并允许 React 能够正确地自动优化你的组
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-1  —  具有副作用的代码应该 与渲染过程分开执行。例如，可以作为 响应事件，在用户与用户界面交互并导致其更新时触发。或者作为一个 Effect，在渲染之后运行。 - 不要修改非局部作用域中的值：组件和 Hoo
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-6  —  val(() => { setTime(new Date()); // ✅ 正确的：非幂等代码不再在渲染中运行。 }, 1000); // 3. 返回一个清理函数，这样我们就不会忘记清理 `setIn
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-7  —  在渲染中 执行，因为 React 可能会多次渲染组件以提供最佳的用户体验。 ### 注意 副作用是一个比 Effect 更广泛的概念。Effect 特指被包裹在 useEffect 中的代码，而“副作
- [ ] vue_guide_essentials_watchers.md-11  —  作用的回调。它们之间的主要区别是追踪响应式依赖的方式： * watch 只追踪明确侦听的数据源。它不会追踪任何在回调中访问到的东西。另外，仅在数据源确实改变时才会触发回调。watch 会避免在发生副作

### 43. [语义改写] 在 React 中，把选中的对象直接存进 state 会带来什么问题，文中建议改成什么做法？

- [x] react_learn_choosing-the-state-structure.md-24  —  }} /> {' '} <button onClick={() => { setSelectedId(item.id); }}>Choose</button> </li> ))} </ul> <p>Y
- [ ] react_learn_preserving-and-resetting-state.md-34  —  用户再次选择前一个收件人时恢复输入 state。对于一个不可见的组件，有几种方法可以让它的 state “活下去”： - 与其只渲染现在这一个聊天，你可以把 所有 聊天都渲染出来，但用 CSS 把其他
- [ ] react_learn_updating-arrays-in-state.md-18  —  段代码中，你先使用 [...list] 展开运算符创建了一份数组的拷贝值。当你有了这个拷贝值后，你就可以使用像 nextList.reverse() 或 nextList.sort() 这样直接修改原
- [ ] react_learn_updating-arrays-in-state.md-31  —  nextSeen;}); ``` 这是因为你并不是在直接修改原始的 state，而是在修改 Immer 提供的一个特殊的 draft 对象。同理，你也可以为 draft 的内容使用 push() 和 
- [ ] react_learn_updating-objects-in-state.md-0  —  学习 React添加交互 Copy pageCopy # 更新 state 中的对象 state 中可以保存任意类型的 JavaScript 值，包括对象。但是，你不应该直接修改存放在 React s
- [ ] react_learn_updating-objects-in-state.md-27  —  。如果你想要写出更简洁的更新处理函数，Immer 会是一个不错的选择，尤其是当你的 state 中有嵌套，并且复制对象会带来重复的代码时。 深入探讨 #### 为什么在 React 中不推荐直接修改 
- [ ] react_learn_updating-objects-in-state.md-28  —  。 - 需求变更：有些应用功能在不出现任何修改的情况下会更容易实现，比如实现撤销/恢复、展示修改历史，或是允许用户把表单重置成某个之前的值。这是因为你可以把 state 之前的拷贝保存到内存中，并适时
- [ ] react_learn_updating-objects-in-state.md-29  —  都视为不可直接修改的。 - 当你在 state 中存放对象时，直接修改对象并不会触发重渲染，并会改变前一次渲染“快照”中 state 的值。 - 不要直接修改一个对象，而要为它创建一个 新 版本，并通

### 44. [命名精确] 按照片段的建议，选中项的状态应该保存为哪个字段？

- [x] react_learn_choosing-the-state-structure.md-24  —  }} /> {' '} <button onClick={() => { setSelectedId(item.id); }}>Choose</button> </li> ))} </ul> <p>Y
- [ ] react_learn_choosing-the-state-structure.md-4  —  </div> ) } ``` 显示更多 另一种你需要将数据整合到一个对象或一个数组的情况是，你不知道未来需要多少个 state 片段。例如，有一个用户可以添加自定义字段的表单时，这将会很有帮助。 ##
- [ ] react_learn_state-a-components-memory.md-10  —  } ``` 显示更多 如果它们不相关，那么存在多个 state 变量是一个好主意，例如本例中的 index 和 showMore。但是，如果你发现经常同时更改两个 state 变量，那么最好将它们合并
- [ ] react_reference_eslint-plugin-react-hooks_lints_config.md-2  —  ] ]}; ``` 查看 配置文档 了解有效选项： ``` // ✅ 更好：有效的配置module.exports = { plugins: [ ['babel-plugin-react-compil
- [ ] react_reference_react-dom_components_input.md-24  —  ug：没有 onChange 事件处理程序的受控多选框<input type="checkbox" checked={something} /> ``` Console你传递了 checked 属性给
- [ ] react_reference_react-dom_components_textarea.md-1  —  制文本框。 - value：一个字符串，用于控制文本框内的文本。 当你传递 value 时，你必须同时传递一个 onChange 处理函数，用于更新传递的值。 如果 <textarea> 是非受控组件
- [ ] react_reference_react_Suspense.md-19  —  态转移是不紧急的，最好继续显示上一页，而不是隐藏任何已经显示的内容。现在点击按钮并等待 Biography 加载： ``` App.jsLayout.jsIndexPage.jsArtistPage.
- [ ] react_reference_react_useEffect.md-51  —  依赖项数组：每次提交后重新运行！ ``` 如果你已经指定了依赖项数组，你的 Effect 仍循环地重新运行，那是因为你的某个依赖项在每次重新渲染时都是不同的。 你可以通过手动打印依赖项到控制台来调试此
- [ ] react_reference_react_useInsertionEffect.md-4  —  态样式使用内联样式）。我们不建议运行时注入 <style> 标签有两个原因： - 运行时注入会使浏览器频繁地重新计算样式。 - 如果在 React 生命周期中某个错误的时机进行运行时注入，它可能会非常
- [ ] react_reference_react_useMemo.md-34  —  visibleTodos = useMemo(() => filterTodos(todos, tab), [todos, tab]); console.log([todos, tab]); ``` 
- [ ] vue_router_zh_guide_advanced_meta.md-1  —  meta: { requiresAuth: false }, }, ], }, ] ``` 那么如何访问这个 meta 字段呢？ 首先，我们称呼 routes 配置中的每个路由对象为 路由记录。路由记

### 45. [概念术语] 为什么在渲染 form 元素的同一个组件里调用 useFormStatus 时，pending 状态始终为 false？

- [x] react_reference_react-dom_hooks_useFormStatus.md-4  —  } export default function App() { return <Form action={submitForm} />; } ``` 显示更多 ### 陷阱 useFormStat
- [ ] react_learn_conditional-rendering.md-7  —  ``` return ( <li className="item"> {isPacked ? name + ' ✅' : name} </li>); ``` 你可以认为，“如果 isPacked 为 
- [ ] react_reference_react-dom_hooks_useFormStatus.md-1  —  tus.pending}>提交</button>}export default function App() { return ( <form action={action}> <Submit /> 
- [ ] react_reference_react-dom_hooks_useFormStatus.md-2  —  没有父级 <form>，它将为 null。 method：字符串，可以是 'get' 或 'post'。表示父级 <form> 使用 GET 或 POST HTTP 方法 进行提交。默认情况下，<fo
- [ ] react_reference_react-dom_hooks_useFormStatus.md-5  —  t() { // ✅ `pending` 将从包裹 Submit 组件的表单派生 const { pending } = useFormStatus(); return <button disable
- [ ] react_reference_react-dom_hooks_useFormStatus.md-7  —  ## 疑难解答 ### status.pending 从不为 true useFormStatus 仅会返回父级 <form> 的状态信息。 如果调用 useFormStatus 的组件未嵌套在 <f
- [ ] react_reference_react_Component.md-13  —  的渲染。在这种情况下即使 render 被调用了两次，用户也无法看到中间的状态。请谨慎使用这种模式因为它可能会造成性能问题。在大多数情况下，你应该能在 constructor 中设置初始的 state
- [ ] react_reference_react_useTransition.md-27  —  , setText] = useState('');// ...function handleChange(e) { // ❌ 不应将受控输入框的状态变量标记为 Transition startTra

### 46. [语义改写] useFormStatus 这个 Hook 只能获取哪一层级表单的状态信息？

- [x] react_reference_react-dom_hooks_useFormStatus.md-4  —  } export default function App() { return <Form action={submitForm} />; } ``` 显示更多 ### 陷阱 useFormStat
- [ ] react_learn_state-a-components-memory.md-5  —  <img src={sculpture.url} alt={sculpture.alt} /> <p> {sculpture.description} </p> </> ); } ``` 显示更多 #
- [ ] react_reference_react-dom_hooks_useFormStatus.md-0  —  API 参考Hook Copy pageCopy # useFormStatus useFormStatus 是一个提供上次表单提交状态信息的 Hook。 ``` const { pending, d
- [ ] react_reference_react-dom_hooks_useFormStatus.md-1  —  tus.pending}>提交</button>}export default function App() { return ( <form action={action}> <Submit /> 
- [ ] react_reference_react-dom_hooks_useFormStatus.md-2  —  没有父级 <form>，它将为 null。 method：字符串，可以是 'get' 或 'post'。表示父级 <form> 使用 GET 或 POST HTTP 方法 进行提交。默认情况下，<fo
- [ ] react_reference_react-dom_hooks_useFormStatus.md-5  —  t() { // ✅ `pending` 将从包裹 Submit 组件的表单派生 const { pending } = useFormStatus(); return <button disable
- [ ] react_reference_react-dom_hooks_useFormStatus.md-7  —  ## 疑难解答 ### status.pending 从不为 true useFormStatus 仅会返回父级 <form> 的状态信息。 如果调用 useFormStatus 的组件未嵌套在 <f

### 47. [命名精确] vue/server-renderer 中用于把应用或 VNode 渲染成 ReadableStream 的函数叫什么名字？

- [x] vue_api_ssr.md-3  —  例。 * 导出自 vue/server-renderer * 类型 ts function renderToWebStream( input: App | VNode, context?: SSRCo
- [ ] react_reference_react-dom_server_renderToReadableStream.md-1  —  Stream 代替。 ## 参考 ### renderToReadableStream(reactNode, options?) 调用 renderToReadableStream，将 React 树
- [ ] vue_api_ssr.md-0  —  # 服务端渲染 API ## renderToString() * 导出自 vue/server-renderer * 类型 ts function renderToString( input: Ap
- [ ] vue_api_ssr.md-1  —  问 Teleport 的内容： js const ctx = {} const html = await renderToString(app, ctx) console.log(ctx.telepo
- [ ] vue_api_ssr.md-2  —  处理函数内 renderToNodeStream(app).pipe(res) vue/server-renderer 的 ESM 构建不支持此方法，因为它是与 Node.js 环境分离的。请换为使用
- [ ] vue_api_ssr.md-4  —  tableStream ): void * 示例 通常与 TransformStream 结合使用： js // 诸如 CloudFlare worker 这样的环境中，TransformStream
- [ ] vue_guide_scaling-up_ssr.md-5  —  如下内容： 1 renderToString() 接收一个 Vue 应用实例作为参数，返回一个 Promise，当 Promise resolve 时得到应用渲染的 HTML。当然你也可以使用 Nod

### 48. [语义改写] 如果运行环境没有全局暴露 ReadableStream 构造函数，应该改用哪个 API 来渲染并输出到 Web WritableStream？

- [x] vue_api_ssr.md-3  —  例。 * 导出自 vue/server-renderer * 类型 ts function renderToWebStream( input: App | VNode, context?: SSRCo
- [ ] react_reference_react-dom_server_renderToReadableStream.md-0  —  API 参考服务端 API Copy pageCopy # renderToReadableStream renderToReadableStream 将 React 树渲染后发送至 Web 可读流。
- [ ] react_reference_react-dom_server_renderToReadableStream.md-1  —  Stream 代替。 ## 参考 ### renderToReadableStream(reactNode, options?) 调用 renderToReadableStream，将 React 树
- [ ] react_reference_react-dom_server_renderToReadableStream.md-4  —  。 - 可选属性 signal：一个 中止信号，用于 中止服务端渲染 并在客户端上渲染其余部分。 #### 返回值 renderToReadableStream 返回一个 Promise： - 如果渲
- [ ] react_reference_react-dom_server_resume.md-0  —  API 参考服务端 API Copy pageCopy # resume resume 将预渲染的 React 树流式传输到 Web 可读流。 ``` const stream = await res
- [ ] react_reference_react-dom_static_prerenderToNodeStream.md-0  —  API 参考Static APIs Copy pageCopy # prerenderToNodeStream prerenderToNodeStream 使用 Node.js 流 将 React 树
- [ ] react_reference_react_useEffect.md-53  —  ，请考虑 完全删除 Effect 函数 是否可以简化你的逻辑。 如果你真的正在与某个外部系统同步，请考虑为什么以及在何种条件下你的 Effect 函数应该更新状态。是否有任何变化会影响组件的可视输出？
- [ ] react_reference_rsc_server-components.md-0  —  API 参考 Copy pageCopy # 服务器组件 服务器组件是一种新型的组件，它在打包之前，在独立于客户端应用程序或 SSR 服务器的环境中提前渲染。 React 服务器组件中的「服务器」就是
- [ ] vue_api_ssr.md-4  —  tableStream ): void * 示例 通常与 TransformStream 结合使用： js // 诸如 CloudFlare worker 这样的环境中，TransformStream

### 49. [命名精确] 这段代码里，用来表示打印状态的那个 React state 变量叫什么名字？

- [x] react_reference_react-dom_flushSync.md-4  —  Printing(true); }) } function handleAfterPrint() { setIsPrinting(false); } window.addEventListener('
- [ ] react_learn_adding-interactivity.md-6  —  ） - 渲染组件（在厨房准备订单） - 提交到 DOM（将订单送到桌前） - Trigger - Render - Commit Rachel Lee Nabors 绘图 ## 想要仔细学习这个主题的
- [ ] react_learn_choosing-the-state-structure.md-7  —  `` 显示更多 尽管这段代码是有效的，但也会让一些 state “极难处理”。例如，如果你忘记同时调用 setIsSent 和 setIsSending，则可能会出现 isSending 和 isSe
- [ ] react_learn_managing-state.md-9  —  并把这些状态移到最近的父级组件，然后通过 props 将状态传递给这两个组件。这被称为“状态提升”，这是编写 React 代码时常做的事。 在以下示例中，要求每次只能激活一个面板。要实现这一点，父组件
- [ ] react_learn_reacting-to-input-with-state.md-6  —  的改变 - 表示内存中的 state（需要使用 useState） - 删除任何不必要的 state 变量 - 连接事件处理函数去设置 state ### 步骤 1：定位组件中不同的视图状态 在计算机
- [ ] react_learn_reacting-to-input-with-state.md-12  —  函数！ 为了可视化这个流程，请尝试在纸上画出圆形标签以表示每个状态，两个状态之间的改变用箭头表示。你可以像这样画出很多流程并且在写代码前解决许多 bug。 表单的各种状态 ### 步骤 3：通过 us
- [ ] react_learn_referencing-values-with-refs.md-2  —  ); } ``` 显示更多 这里的 ref 指向一个数字，但是，像 state 一样，你可以让它指向任何东西：字符串、对象，甚至是函数。与 state 不同的是，ref 是一个普通的 JavaScri
- [ ] react_learn_separating-events-from-effects.md-37  —  ``` Effect Event 是 Effect 代码的非响应式“片段”。他们应该在使用他们的 Effect 的旁边。 ## 摘要 - 事件处理函数在响应特定交互时运行。 - Effect 在需要同
- [ ] react_learn_state-a-components-memory.md-10  —  } ``` 显示更多 如果它们不相关，那么存在多个 state 变量是一个好主意，例如本例中的 index 和 showMore。但是，如果你发现经常同时更改两个 state 变量，那么最好将它们合并
- [ ] react_reference_react-dom_flushSync.md-3  —  打印对话框打开之前立即更改页面。这对于应用自定义打印样式，使文档在打印时能够更好地显示非常有用。在下面的示例中，你在 onbeforeprint 回调函数内调用 flushSync 来立即将 Reac
- [ ] react_reference_react_useState.md-5  —  先前渲染中的信息。请参见下面的示例。 在严格模式中，React 将 两次调用你的更新函数，以帮助你找到 意外的不纯性。这只是开发时的行为，不影响生产。如果你的更新函数是纯函数（本该是这样），就不应影响

### 50. [命名精确] 当打印即将开始时，代码通过哪个事件监听器把打印状态设为 true？

- [x] react_reference_react-dom_flushSync.md-4  —  Printing(true); }) } function handleAfterPrint() { setIsPrinting(false); } window.addEventListener('
- [ ] react_learn_extracting-state-logic-into-a-reducer.md-20  —  nitialTasks = [ {id: 0, text: '参观卡夫卡博物馆', done: true}, {id: 1, text: '看木偶戏', done: false}, {id: 2, t
- [ ] react_learn_extracting-state-logic-into-a-reducer.md-21  —  ，useState 的可读性还行。但是，一旦逻辑变得复杂起来，它们会使组件变得臃肿且难以阅读。在这种情况下，useReducer 允许你将状态更新逻辑与事件处理程序分离开来。 - 可调试性： 当使用 
- [ ] react_learn_removing-effect-dependencies.md-15  —  频繁。 为了找到正确的解决方案，你需要回答关于 Effect 的几个问题。让我们来看看这些问题。 ### 这段代码应该移到事件处理程序中吗？ 你应该考虑的第一件事是，这段代码是否应该成为 Effect
- [ ] react_learn_sharing-state-between-components.md-10  —  on> ); } ``` 显示更多 这样，我们就完成了对状态的提升！将状态移至公共父组件中可以让你更好的管理这两个面板。使用激活索引值代替之前的 是否显示 标识确保了一次只能激活一个面板。而通过向下传
- [ ] react_learn_you-might-not-need-an-effect.md-29  —  你也可以在模块初始化和应用渲染之前执行它： ``` if (typeof window !== 'undefined') { // 检测我们是否在浏览器环境 // ✅ 只在每次应用加载时执行一次 ch
- [ ] react_reference_react-dom_flushSync.md-3  —  打印对话框打开之前立即更改页面。这对于应用自定义打印样式，使文档在打印时能够更好地显示非常有用。在下面的示例中，你在 onbeforeprint 回调函数内调用 flushSync 来立即将 Reac
- [ ] react_reference_react-dom_flushSync.md-5  —  '}</h1> <button onClick={() => window.print()}> 打印 </button> </> ); } ``` 显示更多 如果没有使用 flushSync，打印对话
- [ ] vue_api_composition-api-lifecycle.md-3  —  用，例如计时器、DOM 事件监听器或者与服务器的连接。 这个钩子在服务器端渲染期间不会被调用。 * 示例 vue import { onMounted, onUnmounted } from 'vue
- [ ] vue_api_options-state.md-13  —  息 可以以两种形式声明触发的事件： * 使用字符串数组的简易形式。 * 使用对象的完整形式。该对象的每个属性键是事件的名称，值是 null 或一个验证函数。 验证函数会接收到传递给组件的 $emit 
- [ ] vue_guide_essentials_watchers.md-8  —  持 3.4 及以上版本 每当被侦听源发生变化时，侦听器的回调就会执行。如果希望回调只在源变化时触发一次，请使用 once: true 选项。 js export default { watch: { 

### 51. [命名精确] React 中哪个内置组件能够用来隐藏并恢复其子节点的 UI 和内部状态？

- [x] react_reference_react_components.md-0  —  API 参考 Copy pageCopy # Built-in React Components React 提供了一些内置的组件，你可以在 JSX 中使用它们。 ## 内置组件 - <Fragmen
- [ ] react_reference_react_Activity.md-0  —  API 参考组件 Copy pageCopy # <Activity> <Activity> 允许你隐藏并恢复其子组件的 UI 以及内部状态。 ``` <Activity mode={visibili
- [ ] react_reference_react_Activity.md-1  —  其子组件。同时，React 还会销毁它们的 Effect，并清理所有活跃的订阅。 在隐藏期间，子组件仍会响应新 Props 的变化而进行重新渲染，但其优先级会低于页面上的其他内容。 当边界再次变为 可
- [ ] react_reference_react_Activity.md-2  —  发 ViewTransition 的 enter 动画。如果它变为隐藏，则会触发其 exit 动画。 - 一个处于 hidden 状态、且仅渲染文本内容的 Activity 不会在 DOM 中渲染任何
- [ ] react_reference_react_Activity.md-6  —  eState(true); return ( <> <Activity mode={isShowingSidebar ? 'visible' : 'hidden'}> <Sidebar /> </Ac
- [ ] react_reference_react_Activity.md-10  —  </Activity> <Activity mode={activeTab === 'contact' ? 'visible' : 'hidden'}> <Contact /> </Activity>
- [ ] react_reference_react_Activity.md-30  —  隐藏、但用户很可能很快再次与之交互的 UI 部分保留“瞬时 DOM 状态”的绝佳示例。 我们的示例说明了对于像 <video> 这样的特定标签，卸载和隐藏的行为是不同的。如果一个组件渲染的 DOM 带

### 52. [语义改写] 在 React 里，想以编程方式测量组件树渲染性能，应该使用哪个内置组件？

- [x] react_reference_react_components.md-0  —  API 参考 Copy pageCopy # Built-in React Components React 提供了一些内置的组件，你可以在 JSX 中使用它们。 ## 内置组件 - <Fragmen
- [ ] react_learn_describing-the-ui.md-14  —  t function TeaSet() { return ( <> <Cup guest={1} /> <Cup guest={2} /> <Cup guest={3} /> </> ); } ```
- [ ] react_learn_rendering-lists.md-0  —  学习 React描述 UI Copy pageCopy # 渲染列表 你可能经常需要通过 JavaScript 的数组方法 来操作数组中的数据，从而将一个数据集渲染成多个相似的组件。在这篇文章中，你将
- [ ] react_learn_understanding-your-ui-as-a-tree.md-1  —  用程序中流动以及如何优化呈现和应用程序大小。 ## 渲染树 组件的一个主要特性是能够由其他组件组合而成。在 嵌套组件 中有父组件和子组件的概念，其中每个父组件本身可能是另一个组件的子组件。 当渲染 R
- [ ] react_reference_react-dom_components_title.md-0  —  API 参考组件 Copy pageCopy # <title> 浏览器内置的 <title> 组件 允许向文档指定标题。 ``` <title>我的博客</title> ``` 参考 - <titl
- [ ] react_reference_react_Profiler.md-0  —  API 参考组件 Copy pageCopy # <Profiler> <Profiler> 允许你编程式测量 React 树的渲染性能。 ``` <Profiler id="App" onRende
- [ ] react_reference_react_Profiler.md-2  —  组件树的毫秒数。这可以显示子树在使用记忆化（例如 memo 和 useMemo）后的效果如何。理想情况下，此值在挂载后应显著减少，因为许多后代组件只会在特定的 props 变化时重新渲染。 - bas
- [ ] react_reference_react_Profiler.md-3  —  r={onRender}> <Sidebar /> </Profiler> <PageContent /></App> ``` 这需要两个属性：id（字符串）和 onRender 回调函数（函数），每

### 53. [命名精确] 在组合式 API 中，想让父组件通过 v-model 控制某个 prop，应该调用哪个函数来声明它？

- [x] vue_api_sfc-script-setup.md-10  —  你都可以再传递一个额外的对象，它可以包含 prop 的选项和 model ref 的值转换选项。 js // 声明 "modelValue" prop，由父组件通过 v-model 使用 const 
- [ ] vue_api_sfc-script-setup.md-9  —  llo', labels: () => ['one', 'two'] }) 上面代码会被编译为等价的运行时 props 的 default 选项。此外，withDefaults 辅助函数提供了对默认值
- [ ] vue_api_sfc-script-setup.md-11  —  发 "update:count" 事件 count.value++ } 如果为 defineModel prop 设置了一个 default 值且父组件没有为该 prop 提供任何值，会导致父组件与子
- [ ] vue_guide_components_props.md-11  —  组作为 props 被传入时，虽然子组件无法更改 props 绑定，但仍然可以更改对象或数组内部的值。这是因为 JavaScript 的对象和数组是按引用传递，对 Vue 来说，阻止这种更改需要付出的
- [ ] vue_guide_components_v-mode.md-2  —  件中的 v-model="foo" 将被编译为： vue-html [Parent.vue] <Child :modelValue="foo" @update:modelValue="$event =
- [ ] vue_guide_components_v-model.md-0  —  # 组件 v-model ## 基本用法 v-model 可以在组件上使用以实现双向绑定。 从 Vue 3.4 开始，推荐的实现方式是使用 defineModel() 宏： vue [Child.vu
- [ ] vue_guide_components_v-model.md-2  —  件中的 v-model="foo" 将被编译为： vue-html [Parent.vue] <Child :modelValue="foo" @update:modelValue="$event =

### 54. [语义改写] defineModel 声明 count 这个 prop 时，可以怎样指定它的类型和默认值？

- [x] vue_api_sfc-script-setup.md-10  —  你都可以再传递一个额外的对象，它可以包含 prop 的选项和 model ref 的值转换选项。 js // 声明 "modelValue" prop，由父组件通过 v-model 使用 const 
- [ ] vue_api_sfc-script-setup.md-6  —  ng] }>() * defineProps 或 defineEmits 要么使用运行时声明，要么使用类型声明。同时使用两种声明方式会导致编译报错。 * 使用类型声明的时候，静态分析会自动生成等效的运
- [ ] vue_api_sfc-script-setup.md-9  —  llo', labels: () => ['one', 'two'] }) 上面代码会被编译为等价的运行时 props 的 default 选项。此外，withDefaults 辅助函数提供了对默认值
- [ ] vue_guide_components_props.md-15  —  success', 'warning', 'danger'].includes(value) } }, // 函数类型的默认值 propH: { type: Function, // 不像对象或数组的
- [ ] vue_guide_components_props.md-16  —  efined，都会改为 default 值。 当 prop 的校验失败后，Vue 会抛出一个控制台警告 (在开发模式下)。 如果使用了基于类型的 prop 声明 ，Vue 会尽最大努力在运行时按照 p
- [ ] vue_guide_components_v-mode.md-2  —  件中的 v-model="foo" 将被编译为： vue-html [Parent.vue] <Child :modelValue="foo" @update:modelValue="$event =
- [ ] vue_guide_components_v-model.md-2  —  件中的 v-model="foo" 将被编译为： vue-html [Parent.vue] <Child :modelValue="foo" @update:modelValue="$event =
- [ ] vue_guide_typescript_composition-api.md-2  —  制在 3.3 中得到了解决。最新版本的 Vue 支持在类型参数位置引用导入和有限的复杂类型。但是，由于类型到运行时转换仍然基于 AST，一些需要实际类型分析的复杂类型，例如条件类型，还未支持。你可以使

### 55. [概念术语] 在 Vue 中，当插槽内容需要同时访问父组件和子组件的数据时，应该使用哪种插槽机制？

- [x] vue_guide_components_slots.md-6  —  ter 或 default 的内容存在时，我们希望包装它以提供额外的样式： vue-html 在演练场中尝试一下 ## 动态插槽名 动态指令参数在 v-slot 上也是有效的，即可以定义下面这样的动态
- [ ] vue_guide_built-ins_transition.md-7  —  __bounceOutRight" > hello 在演练场中尝试一下 在演练场中尝试一下 ### 同时使用 transition 和 animation Vue 需要附加事件监听器，以便知道过渡何时
- [ ] vue_guide_components_slots.md-0  —  # 插槽 Slots > 此章节假设你已经看过了组件基础。若你还不了解组件是什么，请先阅读该章节。 ## 插槽内容与出口 在之前的章节中，我们已经了解到组件能够接收任意类型的 JavaScript 值
- [ ] vue_guide_components_slots.md-1  —  avaScript 函数作类比，其概念是类似的： js // 父元素传入插槽内容 FancyButton('Click me!') // FancyButton 在自己的模板中渲染插槽内容 funct
- [ ] vue_guide_components_slots.md-2  —  {{ message }} 这里的两个 {{ message }} 插值表达式渲染的内容都是一样的。 插槽内容无法访问子组件的数据。Vue 模板中的表达式只能访问其定义时所处的作用域，这和 JavaS
- [ ] vue_guide_components_slots.md-3  —  l Save 在演练场中尝试一下 在演练场中尝试一下 ## 具名插槽 有时在一个组件中包含多个插槽出口是很有用的。举例来说，在一个 组件中，有如下模板： vue-html 对于这种场景， 元素可以有一
- [ ] vue_guide_components_slots.md-9  —  bute，不会作为 props 传递给插槽。因此最终 headerProps 的结果是 { message: 'hello' }。 如果你同时使用了具名插槽与默认插槽，则需要为默认插槽使用显式的 标签

### 56. [语义改写] 子组件可以通过什么方式向插槽出口传递数据，让父级模板用 v-slot 接收？

- [x] vue_guide_components_slots.md-6  —  ter 或 default 的内容存在时，我们希望包装它以提供额外的样式： vue-html 在演练场中尝试一下 ## 动态插槽名 动态指令参数在 v-slot 上也是有效的，即可以定义下面这样的动态
- [ ] vue_api_built-in-special-elements.md-2  —  用 v-model 将不起作用： vue import { ref } from 'vue' const tag = ref('input') const username = ref('') 在实践
- [ ] vue_guide_components_slots.md-0  —  # 插槽 Slots > 此章节假设你已经看过了组件基础。若你还不了解组件是什么，请先阅读该章节。 ## 插槽内容与出口 在之前的章节中，我们已经了解到组件能够接收任意类型的 JavaScript 值
- [ ] vue_guide_components_slots.md-3  —  l Save 在演练场中尝试一下 在演练场中尝试一下 ## 具名插槽 有时在一个组件中包含多个插槽出口是很有用的。举例来说，在一个 组件中，有如下模板： vue-html 对于这种场景， 元素可以有一
- [ ] vue_guide_components_slots.md-7  —  nt }} vue-html <slot text="hello" :count="1" /> 使用单个默认插槽和使用具名插槽时，接收插槽 props 的方式略有不同。上面的示例通过在 ChildCo
- [ ] vue_guide_components_slots.md-9  —  bute，不会作为 props 传递给插槽。因此最终 headerProps 的结果是 { message: 'hello' }。 如果你同时使用了具名插槽与默认插槽，则需要为默认插槽使用显式的 标签

### 57. [概念术语] 在 React 中，如何通过标签大小写来区分是使用 HTML 原生标签还是自定义组件？

- [x] react_learn_your-first-component.md-5  —  allery 组件： ``` App.jsApp.jsReloadClearForkfunction Profile() { return ( <img src="https://react.dev/
- [ ] react_learn_describing-the-ui.md-3  —  语言 每个 React 组件都是一个 JavaScript 函数，它可能包含一些标签，React 会将其渲染到浏览器中。React 组件使用一种叫做 JSX 的语法扩展来表示该标签。JSX 看起来很像
- [ ] react_learn_your-first-component.md-0  —  学习 React描述 UI Copy pageCopy # 你的第一个组件 组件 是 React 的核心概念之一。它们是构建用户界面（UI）的基础，是你开始 React 之旅的最佳起点！ ### 你将
- [ ] react_learn_your-first-component.md-1  —  ipt 的）标签——你在 Web 上看到的每一个 UI 模块。 React 允许你将标签、CSS 和 JavaScript 组合成自定义“组件”，即 应用程序中可复用的 UI 元素。上文中表示目录的代
- [ ] vue_api_application.md-12  —  在每个组件的基础上覆盖这些选项。 此配置项仅在完整构建版本，即可以在浏览器中编译模板的 vue.js 文件中可用。如果你用的是带构建的项目配置，且使用的是仅含运行时的 Vue 文件版本，那么编译器选项
- [ ] vue_guide_essentials_component-basics.md-3  —  会以其注册时的名字作为模板中的标签名。 vue import ButtonCounter from './ButtonCounter.vue' Here is a child component! 通
- [ ] vue_guide_essentials_component-basics.md-12  —  比如 Tab 界面： 在演练场中查看示例 在演练场中查看示例 上面的例子是通过 Vue 的 元素和特殊的 is attribute 实现的： vue-html vue-html 在上面的例子中，被传给
- [ ] vue_guide_essentials_component-basics.md-13  —  ML 标签和属性名称是不分大小写的，所以浏览器会把任何大写的字符解释为小写。这意味着当你使用 DOM 内的模板时，无论是 PascalCase 形式的组件名称、camelCase 形式的 prop 名
- [ ] vue_guide_extras_web-components.md-0  —  # Vue 与 Web Components Web Components 是一组 web 原生 API 的统称，允许开发者创建可复用的自定义元素 (custom elements)。 我们认为 Vu

### 58. [命名精确] 示例代码里被重复渲染三次的组件叫什么名字？

- [x] react_learn_your-first-component.md-5  —  allery 组件： ``` App.jsApp.jsReloadClearForkfunction Profile() { return ( <img src="https://react.dev/
- [ ] react_learn_preserving-and-resetting-state.md-16  —  会被添加 并且，当你在相同位置渲染不同的组件时，组件的整个子树都会被重置。要验证这一点，可以增加计数器的值然后勾选复选框： ``` App.jsApp.jsReloadClearForkimport 
- [ ] react_learn_queueing-a-series-of-state-updates.md-0  —  学习 React添加交互 Copy pageCopy # 把一系列 state 更新加入队列 设置组件 state 会把一次重新渲染加入队列。但有时你可能会希望在下次渲染加入队列之前对 state 的
- [ ] react_learn_render-and-commit.md-0  —  学习 React添加交互 Copy pageCopy # 渲染和提交 组件显示到屏幕之前，其必须被 React 渲染。理解这些处理步骤将帮助你思考代码的执行过程并能解释其行为。 ### 你将会学习到 
- [ ] react_learn_reusing-logic-with-custom-hooks.md-8  —  ) { console.log('✅ Progress saved'); } return ( <button disabled={!isOnline} onClick={handleSaveClic
- [ ] react_learn_state-as-a-snapshot.md-4  —  t 收到 setUpdate 通知 - React 更新 state 的值 - React 向组件内传入一张 state 的快照 Rachel Lee Nabors 绘图 这里有个向你展示其运行原理的
- [ ] react_learn_you-might-not-need-an-effect.md-24  —  und > 5) { setIsGameOver(true); } }, [round]); useEffect(() => { alert('游戏结束！'); }, [isGameOver]); f
- [ ] react_reference_react_act.md-3  —  ed {count} times</p> <button onClick={handleClick}> Click me </button> </div> )} ``` ### 在测试中渲染组件 要测
- [ ] react_reference_react_Component.md-35  —  组件在 他们的 state 发生变化时重新渲染。 返回 false 并不能 确保 组件不会重新渲染。React 将使用返回值作为提示，但如果是出于其他有意义的原因，它仍然可能选择重新渲染你的组件。 #
- [ ] react_reference_react_useMemo.md-10  —  用 React 开发者工具分析器 查看哪些组件将从记忆化中获益最多，并在需要的地方添加记忆化。这些原则使你的组件更易于调试和理解，因此在任何情况下都应该遵循它们。从长远来看，我们正在研究 自动进行粒度
- [ ] vue_guide_extras_render-function.md-4  —  ) ] } } 请确保返回的是一个函数而不是一个值！setup() 函数在每个组件中只会被调用一次，而返回的渲染函数将会被调用多次。 我们可以使用 render 选项来声明渲染函数： js impor

### 59. [命名精确] Vue 中哪个内置组件可以把模板片段传送到指定的 DOM 节点，从而避免受父元素样式和层级影响？

- [x] vue_guide_built-ins_telepor.md-2  —  先元素设置了 transform、perspective 或者 filter 样式属性。也就是说如果我们想要用 CSS transform 为祖先节点 设置动画，就会不小心破坏模态框的布局！ * 这个
- [ ] react_reference_react-dom_createPortal.md-5  —  ck"> <p>这个子节点被放置在父节点 div 中。</p> </div> ... </div> <p>这个子节点被放置在 document body 中。</p></body> ``` porta
- [ ] vue_api_built-in-special-elements.md-3  —  的作用域插槽。 元素本身将被其所匹配的插槽内容替换。 Vue 模板里的 元素会被编译到 JavaScript，因此不要与原生 元素进行混淆。 * 参考组件 - 插槽 ## 当我们想要使用内置指令而不在
- [ ] vue_guide_built-ins_teleport.md-2  —  先元素设置了 transform、perspective 或者 filter 样式属性。也就是说如果我们想要用 CSS transform 为祖先节点 设置动画，就会不小心破坏模态框的布局！ * 这个
- [ ] vue_guide_components_slots.md-0  —  # 插槽 Slots > 此章节假设你已经看过了组件基础。若你还不了解组件是什么，请先阅读该章节。 ## 插槽内容与出口 在之前的章节中，我们已经了解到组件能够接收任意类型的 JavaScript 值
- [ ] vue_guide_essentials_template-refs.md-0  —  # 模板引用 虽然 Vue 的声明性渲染模型为你抽象了大部分对 DOM 的直接操作，但在某些情况下，我们仍然需要直接访问底层 DOM 元素。要实现这一点，我们可以使用特殊的 ref attribute
- [ ] vue_guide_extras_rendering-mechanis.md-2  —  遍历返回的虚拟 DOM 树，并基于它创建实际的 DOM 节点。这一步会作为响应式副作用执行，因此它会追踪其中所用到的所有响应式依赖。 3. 更新：当一个依赖发生变化后，副作用会重新运行，这时候会创建一
- [ ] vue_guide_extras_rendering-mechanism.md-2  —  遍历返回的虚拟 DOM 树，并基于它创建实际的 DOM 节点。这一步会作为响应式副作用执行，因此它会追踪其中所用到的所有响应式依赖。 3. 更新：当一个依赖发生变化后，副作用会重新运行，这时候会创建一

### 60. [概念术语] 使用 Vue 的 Teleport 时，通过哪个 prop 来指定传送目标，它的取值可以是什么形式？

- [x] vue_guide_built-ins_telepor.md-2  —  先元素设置了 transform、perspective 或者 filter 样式属性。也就是说如果我们想要用 CSS transform 为祖先节点 设置动画，就会不小心破坏模态框的布局！ * 这个
- [ ] vue_guide_built-ins_telepor.md-3  —  示例。 挂载时，传送的 to 目标必须已经存在于 DOM 中。理想情况下，这应该是整个 Vue 应用外部的一个元素。如果目标元素也是由 Vue 渲染的，你需要确保在挂载 之前先挂载该元素。如果你正在使
- [ ] vue_guide_built-ins_telepor.md-4  —  更新 isMobile。 ## 多个 Teleport 共享目标 一个可重用的 组件可能同时存在多个实例。对于此类场景，多个 组件可以将其内容挂载在同一个目标元素上，而顺序就是简单的顺次追加，后挂载的
- [ ] vue_guide_built-ins_teleport.md-2  —  先元素设置了 transform、perspective 或者 filter 样式属性。也就是说如果我们想要用 CSS transform 为祖先节点 设置动画，就会不小心破坏模态框的布局！ * 这个
- [ ] vue_guide_built-ins_teleport.md-3  —  示例。 挂载时，传送的 to 目标必须已经存在于 DOM 中。理想情况下，这应该是整个 Vue 应用外部的一个元素。如果目标元素也是由 Vue 渲染的，你需要确保在挂载 之前先挂载该元素。如果你正在使
- [ ] vue_guide_built-ins_teleport.md-4  —  更新 isMobile。 ## 多个 Teleport 共享目标 一个可重用的 组件可能同时存在多个实例。对于此类场景，多个 组件可以将其内容挂载在同一个目标元素上，而顺序就是简单的顺次追加，后挂载的
- [ ] vue_guide_typescript_composition-api.md-1  —  数推导出等价的运行时选项。在这种场景下，我们第二个例子中编译出的运行时选项和第一个是完全一致的。 基于类型的声明或者运行时声明可以择一使用，但是不能同时使用。 我们也可以将 props 的类型移入一个

### 61. [命名精确] 表单里的 input 元素是通过哪两个属性来关联无障碍访问名称和描述信息的？

- [x] vue_guide_best-practices_accessibility.md-8  —  " action="/dataCollectionLocation" method="post" autocomplete="on" > Billing Full Name: <input type=
- [ ] vue_guide_best-practices_accessibility.md-4  —  e="complementary" | 用来支持主内容，同时其自身的内容是相对独立且有意义的 | | search | role="search" | 该章节包含整个应用的搜索功能 | | form 
- [ ] vue_guide_best-practices_accessibility.md-5  —  表单中的所有 input 框。你也可以为每个 input 框都设置不同的 autocomplete attribute 的值。 ### 标签 提供标签来描述所有表单控件的用途；使 for 和 id 链
- [ ] vue_guide_best-practices_accessibility.md-6  —  v-model="name" :aria-label="nameLabel" /> 在 Chrome DevTools 中审查此元素，查看无障碍名称是如何更改的： !Chrome 开发者工具正在通过 
- [ ] vue_guide_best-practices_accessibility.md-7  —  具通过 aria-labelledby 展示 input 的无障碍访问名称 在可复用组件中使用这种模式时，请使用 useId() 生成 ID，而不是硬编码它们。这样可以在保持每个组件实例的 id 值唯
- [ ] vue_guide_best-practices_accessibility.md-12  —  ip-path: inset(100%); } #### aria-hidden="true" 添加 aria-hidden="true" 在无障碍访问时被隐藏，但对其他可视用户仍然是可见的。不要在可
- [ ] vue_guide_best-practices_accessibility.md-13  —  mg.icons8.com/search" alt="Search" /> * 图标 vue-html Search: Search ## 规范 万维网联盟 (W3C) Web 无障碍访问倡议 (WA

### 62. [语义改写] 为什么不建议在表单中使用占位符文本？

- [x] vue_guide_best-practices_accessibility.md-8  —  " action="/dataCollectionLocation" method="post" autocomplete="on" > Billing Full Name: <input type=
- [ ] react_learn_preserving-and-resetting-state.md-35  —  <Chat> 树指定一个 key 是合理的。 ## 摘要 - 只要在相同位置渲染的是相同组件， React 就会保留状态。 - state 不会被保存在 JSX 标签里。它与你在树中放置该 JSX 的
- [ ] react_reference_react-dom_components_textarea.md-3  —  idCapture：与 onInvalid 类似，但是是在 捕获阶段 触发。 - onSelect：一个 Event 处理函数。当 <textarea> 的选择内容发生变化后触发。React 扩展了 
- [ ] react_reference_react-dom_components_textarea.md-7  —  ols={40} /> </label> ); } ``` ### 陷阱 与 HTML 不同，像这样传递初始值 <textarea>Some content</textarea> 将不受支持。 ###
- [ ] react_reference_react-dom_components_textarea.md-13  —  value={something} /> ``` Console如果在没有提供 onChange 处理程序的情况下向表单字段提供了 value 属性，这将导致文本框只读。如果文本框的内容是可变的，请使
- [ ] react_reference_rsc_use-client.md-1  —  or({ timestamp, text }) { const date = formatDate(timestamp); // ... const editButton = <Button />; 
- [ ] vue_api_component-instance.md-1  —  挂载完成 (mounted) 之前都会是 undefined。 * 对于单一根元素的组件，$el 将会指向该根元素。 * 对于以文本节点为根的组件，$el 将会指向该文本节点。 * 对于以多个元素为根
- [ ] vue_guide_best-practices_accessibility.md-9  —  input 框中的数据一样。查看以下示例，可以看到满足颜色对比度条件的姓氏占位符看起来像预填充的数据： !可访问的占位文本 vue-html <form class="demo" action="/d

### 63. [语义改写] 在 React 组件中，ref 的读取和写入操作应该放在哪里才符合规范？

- [x] react_reference_react_useRef.md-6  —  // 🚩 不要在渲染期间写入 ref myRef.current = 123; // ... // 🚩 不要在渲染期间读取 ref return <h1>{myOtherRef.current}</h
- [ ] react_learn_escape-hatches.md-2  —  可以使用 ref 来存储 timeout ID、DOM 元素 和其他不影响组件渲染输出的对象。 ## 想要仔细学习这个主题的内容吗？ 阅读 使用 ref 引用值 以了解如何使用 ref 来记住信息。 
- [ ] react_learn_referencing-values-with-refs.md-11  —  其视为没有设置函数的常规 state 变量。 如果你熟悉面向对象编程，ref 可能会让你想起实例字段 —— 但是你写的不是 this.something，而是 somethingRef.current
- [ ] react_learn_referencing-values-with-refs.md-13  —  OM 元素。例如，如果你想以编程方式聚焦一个输入框，这种用法就会派上用场。当你将 ref 传递给 JSX 中的 ref 属性时，比如 <div ref={myRef}>，React 会将相应的 DOM
- [ ] react_learn_separating-events-from-effects.md-1  —  件应该自动连接选中的聊天室。 - 每当你点击“Send”按钮，组件应该在当前聊天界面发送一条消息。 假设你已经实现了这部分代码，但是还没有确定应该放在哪里。你是应该用事件处理函数还是 Effect 呢
- [ ] react_reference_react-dom_components_link.md-4  —  哪个位置被渲染，React 都会始终将其对应的 DOM 元素放在文档的 <head> 中。<head> 是 <link> 在 DOM 中唯一有效的位置，但如果表示特定页面的组件可以自行渲染 <link
- [ ] react_reference_react_useRef.md-5  —  rrent + 1; alert('You clicked ' + ref.current + ' times!'); } return ( <button onClick={handleClick}
- [ ] vue_api_built-in-special-attributes.md-1  —  触发。 * 参考指南 - 列表渲染 - 通过 key 管理状态 ## ref 用于注册模板引用。 * 预期：string | Function * 详细信息 ref 用于注册元素或子组件的引用。 使用

### 64. [概念术语] 如果确实需要在渲染过程中读取或写入 ref，React 官方建议改用哪种方式？

- [x] react_reference_react_useRef.md-6  —  // 🚩 不要在渲染期间写入 ref myRef.current = 123; // ... // 🚩 不要在渲染期间读取 ref return <h1>{myOtherRef.current}</h
- [ ] react_learn_referencing-values-with-refs.md-7  —  处理器需要，并且更改它不需要重新渲染时，使用 ref 可能会更高效。 ## ref 和 state 的不同之处 也许你觉得 ref 似乎没有 state 那样“严格” —— 例如，你可以改变它们而非总
- [ ] react_learn_referencing-values-with-refs.md-11  —  其视为没有设置函数的常规 state 变量。 如果你熟悉面向对象编程，ref 可能会让你想起实例字段 —— 但是你写的不是 this.something，而是 somethingRef.current
- [ ] react_learn_referencing-values-with-refs.md-12  —  某些信息，请使用 state 代替。由于 React 不知道 ref.current 何时发生变化，即使在渲染时读取它也会使组件的行为难以预测。（唯一的例外是像 if (!ref.current) r
- [ ] react_learn_referencing-values-with-refs.md-13  —  OM 元素。例如，如果你想以编程方式聚焦一个输入框，这种用法就会派上用场。当你将 ref 传递给 JSX 中的 ref 属性时，比如 <div ref={myRef}>，React 会将相应的 DOM
- [ ] react_learn_render-and-commit.md-4  —  程中, React 将计算它们的哪些属性（如果有的话）自上次渲染以来已更改。在下一步（提交阶段）之前，它不会对这些信息执行任何操作。 ### 陷阱 渲染必须始终是一次 纯计算: - 输入相同，输出相同
- [ ] react_reference_react_useRef.md-5  —  rrent + 1; alert('You clicked ' + ref.current + ' times!'); } return ( <button onClick={handleClick}
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-2  —  你想要渲染的内容，React 会自己选择最佳的方式向用户展示它。为了做到这一点，React 在执行你的代码时分为几个阶段。虽然你不必了解所有这些阶段就能很好地使用 React。但是，了解哪些代码在渲染

### 65. [命名精确] 在排查 React 编译器相关问题时，如何临时跳过某个组件的编译？

- [x] react_learn_react-compiler_debugging.md-2  —  。请将以下信息报告到 facebook/react 仓库： - 错误信息 - 导致错误的代码 - 你使用的 React 和编译器版本 ### 运行时问题 关于运行时行为问题： ### 1. 临时禁用编
- [ ] react_learn_react-compiler_debugging.md-0  —  学习 ReactReact Compiler Copy pageCopy # 调试和故障排除 本指南可帮助你在使用 React 编译器时识别和修复问题。学习如何调试编译问题并解决常见错误。 ### 你
- [ ] react_learn_react-compiler_debugging.md-1  —  中查找 ESLint 规则未能检测到的 React 规则违规情况。编译器依赖于你的代码遵循这些规则，当规则被违反且编译器无法检测到时，就会出现运行时问题。 ## 常见的破坏性模式 React Comp
- [ ] react_learn_react-compiler_incremental-adoption.md-1  —  何违反 React 规则的问题。你可以在扩展编译器覆盖范围的同时有条不紊地解决这些问题，而不是一次性修复整个代码库中的违规问题。这使迁移过程更易于管理，并降低了引入错误的风险。 通过控制代码中哪些部分
- [ ] react_learn_react-compiler_installation.md-9  —  器跳过对该特定组件的优化。你应该修复根本问题，并在解决后移除该指令。 如需更多故障排除帮助，请参阅调试指南。 ## 下一步 既然你已经安装了 React 编译器，可以进一步了解以下内容： - Reac
- [ ] react_reference_react-compiler_directives.md-4  —  ; // TODO: 待 ThirdPartyLib 升级到 v2.0 后移除 return <ThirdPartyComponent />;} ``` ## 常见模式 ### 渐进式引入 在大型代码
- [ ] react_reference_react-compiler_directives_use-memo.md-5  —  编译。 ## 故障排除 ### 验证优化效果 要确认你的组件是否被成功优化，可以： - 检查你构建产物中被编译后的输出代码 - 使用 React 开发工具检查组件是否带有 Memo ✨ 徽章 ### 
- [ ] react_reference_react-compiler_directives_use-no-memo.md-1  —  反引号。 - 该指令必须与 "use no memo" 或其别名 "use no forget" 完全匹配。 - 该指令的优先级高于所有编译模式和其他指令。 - 它旨在作为一种临时的调试工具，而非永久

### 66. [语义改写] 如果移除组件中所有手动的 memoization 后问题依然存在，说明什么？

- [x] react_learn_react-compiler_debugging.md-2  —  。请将以下信息报告到 facebook/react 仓库： - 错误信息 - 导致错误的代码 - 你使用的 React 和编译器版本 ### 运行时问题 关于运行时行为问题： ### 1. 临时禁用编
- [ ] react_learn_react-compiler_introduction.md-0  —  学习 ReactReact Compiler Copy pageCopy # 介绍 React 编译器是一个新的构建时工具，它可以自动优化你的 React 应用。它支持纯 JavaScript，并且了
- [ ] react_learn_reacting-to-input-with-state.md-14  —  不代表任何你希望用户看到的有效 UI 的情况。（比如你绝对不会想要在展示错误信息的同时禁用掉输入框，导致用户无法纠正错误！） 这有一些你可以问自己的， 关于 state 变量的问题： - 这个 sta
- [ ] react_reference_react_memo.md-0  —  API 参考API Copy pageCopy # memo memo 允许你的组件在 props 没有改变的情况下跳过重新渲染。 ``` const MemoizedComponent = memo
- [ ] react_reference_react_memo.md-6  —  如果传递给组件的 props 始终不同，例如在渲染期间传递对象或普通函数，则 memo 是完全无用的。这就是为什么你通常需要在 memo 中同时使用 useMemo 和 useCallback。 在其
- [ ] react_reference_react_memo.md-7  —  显的视觉瑕疵，则这是你组件中的 bug！修复 bug 而不是添加 memoization。 - 避免 不必要的 Effect 来更新状态。React 应用中的大多数性能问题都是由于 Effect 引起
- [ ] vue_api_built-in-directives.md-12  —  oak 会保留在所绑定的元素上，直到相关组件实例被挂载后才移除。配合像 [v-cloak] { display: none } 这样的 CSS 规则，它可以在组件编译完毕前隐藏原始模板。 * 示例 c
- [ ] vue_guide_extras_web-components.md-5  —  k 初次调用时，一个 Vue 自定义元素会在内部挂载一个 Vue 组件实例到它的 shadow root 上。 * 当此元素的 disconnectedCallback 被调用时，Vue 会在一个微任

### 67. [概念术语] Vue 的浏览器开发者插件能帮开发者做哪些事情？

- [x] vue_guide_scaling-up_tooling.md-4  —  lar 支持。 * vim / Neovim 通过 coc-volar 支持。 * emacs 通过 lsp-mode 支持。 ## 浏览器开发者插件 Vue 的浏览器开发者插件使我们可以浏览一个 V
- [ ] react_learn_react-compiler_introduction.md-8  —  编译器构建的一个轻量级 Babel 插件封装，其设计初衷是为了与 Babel 本身解耦。尽管编译器的第一个稳定版本主要仍然是一个 Babel 插件，但我们正在与 swc 和 oxc 团队合作，为 Re
- [ ] vue_about_faq.md-2  —  我们也理解可能会有无法在此时间轴上升级的团队或项目仍需满足其安全及合规需求。我们正在与业内专家合作为有这种需求的团队提供 Vue 2 的扩展支持——如果您的团队预期在 2023 年底之后仍然需要使用 
- [ ] vue_about_faq.md-5  —  如 Svelte 的框架使用了一种为单个组件产生极轻量级输出的编译策略。然而，我们的研究表明，包大小的差异在很大程度上取决于应用中的组件数量。虽然 Vue 的基线大小更重，但它生成的每个组件的代码更少
- [ ] vue_guide_best-practices_performance.md-1  —  一步是为你的应用类型确定合适的架构： * 查看使用 Vue 的多种方式这一章看看如何用不同的方式围绕 Vue 组织架构。 * Jason Miller 在 Application Holotypes 
- [ ] vue_guide_best-practices_security.md-6  —  每个 HTML 元素都有能接受字符串形式 JavaScript 的 attribute，例如 onclick、onfocus 和 onmouseenter。绑定任何用户提供的 JavaScript 给
- [ ] vue_guide_extras_ways-of-using-vue.md-2  —  型的同时获得 SPA 的益处。 ## 全栈 / SSR 纯客户端的 SPA 在首屏加载和 SEO 方面有显著的问题，因为浏览器会收到一个巨大的 HTML 空页面，只有等到 JavaScript 加载完
- [ ] vue_guide_extras_ways-of-using-vue.md-4  —  于它构建的，并且支持两种形式的 SSG！此外，也可以看看其他通常支持 SSG 的 Vue 框架。 ## Web 之外... 尽管 Vue 主要是为构建 Web 应用而设计的，但它绝不仅仅局限于浏览器。
- [ ] vue_guide_scaling-up_tooling.md-3  —  因为某些原因，在有构建步骤时，你仍需要浏览器内的模板编译，你可以更改构建工具配置，将 vue 改为相应的版本 vue/dist/vue.esm-bundler.js。 如果你需要一种更轻量级，不依赖构

### 68. [命名精确] 想在命令行对单文件组件执行类型检查并生成 d.ts 文件，应该用哪个工具？

- [x] vue_guide_scaling-up_tooling.md-4  —  lar 支持。 * vim / Neovim 通过 coc-volar 支持。 * emacs 通过 lsp-mode 支持。 ## 浏览器开发者插件 Vue 的浏览器开发者插件使我们可以浏览一个 V
- [ ] vue_api_composition-api-setup.md-4  —  ts.x 的形式使用其中的属性。此外还需注意，和 props 不同，attrs 和 slots 的属性都不是响应式的。如果你想要基于 attrs 或 slots 的改变来执行副作用，那么你应该在 on
- [ ] vue_api_utility-types.md-4  —  类型扩展必须被放置在一个模块 .ts 或 .d.ts 文件中。查看类型扩展指南了解更多细节。 * 参考指南 - 扩展自定义选项 ## ComponentCustomProps 用于扩展全局可用的 TS
- [ ] vue_api_utility-types.md-5  —  : --${string}]: string } } tsx html 类型增强必须被放置在一个模块 .ts 或 .d.ts 文件中。查看类型增强指南了解更多细节。 单文件组件 标签支持通过 v-bi
- [ ] vue_guide_typescript_options-api.md-8  —  erties 接口： ts import axios from 'axios' declare module 'vue' { interface ComponentCustomProperties {
- [ ] vue_guide_typescript_overview.md-0  —  # 搭配 TypeScript 使用 Vue 像 TypeScript 这样的类型系统可以在编译时通过静态分析检测出很多常见错误。这减少了生产环境中的运行时错误，也让我们在重构大型项目的时候更有信心。
- [ ] vue_guide_typescript_overview.md-1  —  单文件组件，你可以使用工具 vue-tsc 在命令行检查类型和生成类型声明文件。vue-tsc 是对 TypeScript 自身命令行界面 tsc 的一个封装。它的工作方式基本和 tsc 一致。除了 
- [ ] vue_guide_typescript_overview.md-5  —  e-tsc 中看到的基于源代码的错误提示并不一致。 * 类型检查可能会很慢。当它和代码转换在相同的线程/进程中执行时，它会显著影响整个应用的构建速度。 * 我们已经在 IDE 中通过单独的进程运行着类
- [ ] vue_guide_typescript_overview.md-7  —  对 defineComponent 的类型测试 defineComponent() 也支持对纯 JavaScript 编写的组件进行类型推导。 ### 在单文件组件中的用法 要在单文件组件中使用 Ty

### 69. [概念术语] 在 Vue Router 中，path 和 params 能同时出现在一个路由对象里吗？

- [x] vue_router_zh_guide_essentials_navigation.md-3  —  `params` 不能与 `path` 一起使用 router.push({ path: '/user', params: { username } }) // -> /user ``` 构建字符串路
- [ ] vue_router_zh_api_interfaces_RouteLocationNormalizedLoaded.md-1  —  mponents 对象内被替换掉的懒加载组件)。所以它可以被直接用于展示路由。同样它不包含重定向的记录。 ### meta • meta: RouteMeta 从所有匹配的路由记录中合并的 meta 
- [ ] vue_router_zh_guide_advanced_lazy-loading.md-0  —  # 路由懒加载 在 Vue School 上观看免费视频课程 当打包构建应用时，JavaScript 包会变得非常大，影响页面加载。如果我们能把不同路由对应的组件分割成不同的代码块，然后当路由被访问的
- [ ] vue_router_zh_guide_advanced_meta.md-1  —  meta: { requiresAuth: false }, }, ], }, ] ``` 那么如何访问这个 meta 字段呢？ 首先，我们称呼 routes 配置中的每个路由对象为 路由记录。路由记
- [ ] vue_router_zh_guide_advanced_typed-routes.md-2  —  'named-param-edit', '/:name/edit', { name: string | number }, // 我们还需要包含父级路由的参数 { name: string }, ne
- [ ] vue_router_zh_guide_essentials_dynamic-matching.md-0  —  # 带参数的动态路由匹配 在 Vue School 上观看免费视频课程 很多时候，我们需要将给定匹配模式的路由映射到同一个组件。例如，我们可能有一个 User 组件，它应该对所有用户进行渲染，但用户 
- [ ] vue_router_zh_guide_essentials_dynamic-matching.md-1  —  ： ``` vue<template> <div> <!-- 当前路由可以通过 $route 在模板中访问 --> User {{ $route.params.id }} </div> </templ
- [ ] vue_router_zh_guide_essentials_named-routes.md-0  —  # 命名路由 在 Vue School 上观看免费视频课程 当创建一个路由时，我们可以选择给路由一个 name： ``` jsconst routes = [ { path: '/user/:user
- [ ] vue_router_zh_guide_essentials_nested-routes.md-1  —  ──────────┘ │ │ └──────────────┘ │ └──────────────────┘ └──────────────────┘ ``` 通过 Vue Router，你可以使用

### 70. [语义改写] 用 RouterLink 传参时，如果已经存在对应的命名路由，官方推荐用哪种写法？

- [x] vue_router_zh_guide_essentials_navigation.md-3  —  `params` 不能与 `path` 一起使用 router.push({ path: '/user', params: { username } }) // -> /user ``` 构建字符串路
- [ ] vue_router_zh_guide_advanced_composition-api.md-3  —  st userData = ref() // 与 beforeRouteUpdate 相同，无法访问 `this` onBeforeRouteUpdate(async (to, from) => { 
- [ ] vue_router_zh_guide_advanced_composition-api.md-4  —  自定义链接： ``` vue<script setup> import { RouterLink, useLink } from 'vue-router' import { computed } fr
- [ ] vue_router_zh_guide_advanced_router-view-slot.md-3  —  /> </router-view> ``` 而如果我们将引用放在 <router-view> 上，那引用将会被 RouterView 的实例填充，而不是路由组件本身。
- [ ] vue_router_zh_guide_advanced_typed-routes.md-2  —  'named-param-edit', '/:name/edit', { name: string | number }, // 我们还需要包含父级路由的参数 { name: string }, ne
- [ ] vue_router_zh_guide_essentials_active-links.md-0  —  # 匹配当前路由的链接 应用程序通常都会有一个渲染 RouterLink 列表的导航组件。我们也许想对这个列表中匹配当前路由的链接进行视觉区分。 RouterLink 组件会为匹配当前路由的链接添加两
- [ ] vue_router_zh_guide_essentials_active-links.md-1  —  一个路由有 redirect，在检查链接是否匹配当前路由时不会跟随重定向。 ## 精确匹配当前路由的链接 精确匹配不包括祖先路由。 假设我们有以下路由： ``` jsconst routes = [ 
- [ ] vue_router_zh_guide_essentials_dynamic-matching.md-1  —  ： ``` vue<template> <div> <!-- 当前路由可以通过 $route 在模板中访问 --> User {{ $route.params.id }} </div> </templ
- [ ] vue_router_zh_guide_essentials_named-routes.md-0  —  # 命名路由 在 Vue School 上观看免费视频课程 当创建一个路由时，我们可以选择给路由一个 name： ``` jsconst routes = [ { path: '/user/:user
- [ ] vue_router_zh_guide_essentials_navigation.md-2  —  这种情况。取而代之的是下面例子的做法，你需要提供路由的 name 或手写完整的带有参数的 path ： ``` jsconst username = 'eduardo/san martin' // 我

### 71. [命名精确] 在浏览器端渲染 React 组件时，应该从哪个模块引入相关接口？

- [x] react_reference_react-dom_client.md-0  —  API 参考 Copy pageCopy # Client React DOM API react-dom/client API 允许你在客户端（浏览器）渲染 React 组件。这些 API 通常在应
- [ ] react_learn_describing-the-ui.md-9  —  想要仔细学习这个主题的内容吗？ 请参阅 将 Props 传递给组件 以了解如何传递并读取 props。 阅读更多 ## 条件渲染 你的组件经常需要根据不同的条件来显示不同的东西。在 React 中，你
- [ ] react_learn_state-a-components-memory.md-10  —  } ``` 显示更多 如果它们不相关，那么存在多个 state 变量是一个好主意，例如本例中的 index 和 showMore。但是，如果你发现经常同时更改两个 state 变量，那么最好将它们合并
- [ ] react_learn_understanding-your-ui-as-a-tree.md-0  —  学习 React描述 UI Copy pageCopy # 将 UI 视为树 当 React 应用程序逐渐成形时，许多组件会出现嵌套。那么 React 是如何跟踪应用程序组件结构的？ React 以及
- [ ] react_reference_react-dom_server_renderToPipeableStream.md-2  —  务端生成的 HTML 中的绑定事件生效，进而让其变得可交互。 参见下方更多示例。 #### 参数 reactNode：想要将其渲染为 HTML 的 React 节点，比如像 <App /> 这样的 J
- [ ] react_reference_react-dom_server_renderToReadableStream.md-2  —  更多示例。 #### 参数 reactNode：要渲染为 HTML 的 React 节点。例如，类似 <App /> 的 JSX 元素。它应该表示整个文档，因此 App 组件应该渲染 <html> 标
- [ ] react_reference_react-dom_static_prerenderToNodeStream.md-2  —  变为可交互。 详见下面的更多示例。 #### 参数 reactNode：要渲染为 HTML 的 React 节点。例如 JSX 节点 <App />。它应代表整个文档，因此 App 组件应渲染 <ht
- [ ] react_reference_rsc_use-client.md-2  —  件模块包含 'use client' 指示符时，保证对该组件的任何使用都将是客户端组件。然而，即使没有 'use client' 指示符，组件仍可以在客户端上进行评估。 - 如果组件是在带有 'use
- [ ] react_reference_rsc_use-client.md-4  —  nspirationGenerator> </> ); } ``` 在这个示例应用程序的模块依赖树中，InspirationGenerator.js 中的 'use client' 指示符标记了该模块
- [ ] vue_guide_components_slots.md-0  —  # 插槽 Slots > 此章节假设你已经看过了组件基础。若你还不了解组件是什么，请先阅读该章节。 ## 插槽内容与出口 在之前的章节中，我们已经了解到组件能够接收任意类型的 JavaScript 值
- [ ] vue_guide_scaling-up_testing.md-12  —  一个预上线的环境中运行。针对预上线环境的测试不仅包括你的前端代码和静态服务器，还包括所有相关的后端服务和基础设施。 > 你的测试越是类似于你的软件的使用方式，它们就越能值得你信赖。- Kent C. 

### 72. [数字精确] React 最低支持到哪个版本的 Internet Explorer，旧版本又该如何处理？

- [x] react_reference_react-dom_client.md-0  —  API 参考 Copy pageCopy # Client React DOM API react-dom/client API 允许你在客户端（浏览器）渲染 React 组件。这些 API 通常在应
- [ ] react_learn_react-compiler_installation.md-2  —  高版本，那么可以从 @vitejs/plugin-react 中导出并配置 reactCompilerPreset： ``` Terminal Copynpm install -D @rolldown
- [ ] react_learn_react-compiler_installation.md-3  —  Babel 选项已经被移除。如果你使用的是更低版本，可以通过下面的方式进行配置： ``` // vite.config.jsimport { defineConfig } from 'vite';im
- [ ] react_learn_react-compiler_installation.md-9  —  器跳过对该特定组件的优化。你应该修复根本问题，并在解决后移除该指令。 如需更多故障排除帮助，请参阅调试指南。 ## 下一步 既然你已经安装了 React 编译器，可以进一步了解以下内容： - Reac
- [ ] react_learn_react-compiler_introduction.md-0  —  学习 ReactReact Compiler Copy pageCopy # 介绍 React 编译器是一个新的构建时工具，它可以自动优化你的 React 应用。它支持纯 JavaScript，并且了
- [ ] react_learn_react-developer-tools.md-1  —  `` react-devtools ``` 然后通过将以下 <script> 标签添加到你网站的 <head> 开头来连接你的网站： ``` <html> <head> <script src="ht
- [ ] react_reference_react-compiler_compiling-libraries.md-1  —  ompiler@latest ``` 配置你的构建工具来编译你的库。例如，使用 Babel： ``` // babel.config.jsmodule.exports = { plugins: [ '
- [ ] react_reference_react-compiler_compiling-libraries.md-2  —  0.0" }} ``` ### 2. 配置目标版本 设置你的库所支持的最低 React 版本： ``` { target: '17', // 最低支持的 React 版本} ``` ## 测试策略 为
- [ ] vue_about_faq.md-2  —  我们也理解可能会有无法在此时间轴上升级的团队或项目仍需满足其安全及合规需求。我们正在与业内专家合作为有这种需求的团队提供 Vue 2 的扩展支持——如果您的团队预期在 2023 年底之后仍然需要使用 

### 73. [语义改写] 在 Vue 里，如果没有使用 <script setup>，要怎么把导入的组件注册到当前组件中才能使用？

- [x] vue_guide_components_registration.md-2  —  依赖关系更加明确，并且对 tree-shaking 更加友好。 在使用 的单文件组件中，导入的组件可以直接在模板中使用，无需注册： vue import ComponentA from './Comp
- [ ] vue_api_sfc-script-setup.md-19  —  c 来显式指定： vue 为了在 ref 中使用泛型组件的引用，你需要使用 vue-component-type-helpers 库，因为 InstanceType 在这种场景下不起作用。 vue <
- [ ] vue_api_sfc-spec.md-3  —  lor: #333; body { color: $primary-color; } 注意对不同预处理器的集成会根据你所使用的工具链而有所不同，具体细节请查看相应的工具链文档来确认： * Vite *
- [ ] vue_guide_components_registration.md-0  —  # 组件注册 > 此章节假设你已经看过了组件基础。若你还不了解组件是什么，请先阅读该章节。 一个 Vue 组件在使用前需要先被“注册”，这样 Vue 才能在渲染模板时找到其对应的实现。组件注册有两种方
- [ ] vue_guide_essentials_component-basics.md-2  —  可以使用 ID 选择器来指向一个元素 (通常是原生的 元素)，Vue 将会使用其内容作为模板来源。 上面的例子中定义了一个组件，并在一个 .js 文件里默认导出了它自己，但你也可以通过具名导出在一个文
- [ ] vue_guide_essentials_component-basics.md-3  —  会以其注册时的名字作为模板中的标签名。 vue import ButtonCounter from './ButtonCounter.vue' Here is a child component! 通
- [ ] vue_guide_essentials_lifecycle.md-1  —  参考及其用法请参考 API 索引。mounted、updated 和 unmounted。 所有生命周期钩子函数的 this 上下文都会自动指向当前调用它的组件实例。注意：避免用箭头函数来定义生命周期
- [ ] vue_router_zh_guide_advanced_composition-api.md-0  —  # Vue Router 和 组合式 API 在 Vue School 上观看免费视频课程 Vue 的组合式 API 的引入开辟了新的可能性，但要想充分发挥 Vue Router 的潜力，我们需要使用

### 74. [概念术语] components 选项对象中，属性名和属性值分别代表什么含义？

- [x] vue_guide_components_registration.md-2  —  依赖关系更加明确，并且对 tree-shaking 更加友好。 在使用 的单文件组件中，导入的组件可以直接在模板中使用，无需注册： vue import ComponentA from './Comp
- [ ] react_reference_react-dom_components_option.md-1  —  ops <option> 支持所有 常见的元素属性。 除此之外，<option> 还支持以下属性： - disabled：布尔值。如果 disabled 为 true，该选项（option）将会被选中
- [ ] react_reference_react-dom_components_option.md-2  —  ption> 都设置一个 value 属性，表示要与表单一起提交的数据。 在这里了解更多关于 如何展示一个包含一系列 <option> 组件的 <select> 的信息。 ``` App.jsApp.
- [ ] vue_api_options-composition.md-2  —  个对象，其 key 名就是在当前组件中的本地绑定名称，而它的值应该是以下两种之一： * 匹配可用注入的 key (string 或者 Symbol) * 一个对象 * 它的 from 属性是一个 ke
- [ ] vue_api_options-misc.md-0  —  # 其他杂项选项 ## name 用于显式声明组件展示时的名称。 * 类型 ts interface ComponentOptions { name?: string } * 详细信息 组件的名字有以
- [ ] vue_guide_components_provide-injec.md-5  —  之前被解析，因此你可以在 data() 中访问到注入的属性： js export default { inject: ['message'], data() { return { // 基于注入值的初
- [ ] vue_guide_components_provide-inject.md-5  —  之前被解析，因此你可以在 data() 中访问到注入的属性： js export default { inject: ['message'], data() { return { // 基于注入值的初
- [ ] vue_guide_essentials_reactivity-fundamentals.md-0  —  # 响应式基础 本页和后面很多页面中都分别包含了选项式 API 和组合式 API 的示例代码。现在你选择的是 选项式 API组合式 API。你可以使用左侧侧边栏顶部的“API 风格偏好”开关在 API

### 75. [概念术语] 在 React 的 useEffect 中，返回的那个函数会在什么时机被调用？

- [x] react_learn_synchronizing-with-effects.md-25  —  。 ``` useEffect(() => { const connection = createConnection(); connection.connect(); return () => { 
- [ ] react_learn_queueing-a-series-of-state-updates.md-5  —  => n + 1 是一个函数。React 将它加入队列。 当你在下次渲染期间调用 useState 时，React 会遍历队列。之前的 number state 的值是 0，所以这就是 React 作
- [ ] react_learn_render-and-commit.md-2  —  的胃口。） - 状态更新... - ...触发... - ...渲染! Rachel Lee Nabors 绘图 ## 步骤 2: React 渲染你的组件 在你触发渲染后，React 会调用你的组件
- [ ] react_learn_reusing-logic-with-custom-hooks.md-0  —  学习 React脱围机制 Copy pageCopy # 使用自定义 Hook 复用逻辑 React 有一些内置 Hook，例如 useState，useContext 和 useEffect。有时你
- [ ] react_reference_react-dom_flushSync.md-6  —  已经在渲染时，React 无法刷新。考虑将此调用移至调度器任务或微任务中。 这包括在以下场景中调用 flushSync： - 渲染组件时。 - useLayoutEffect 或 useEffect 
- [ ] react_reference_react_useCallback.md-2  —  新一次渲染中传入的函数，并且将其缓存以便之后使用。React 不会调用此函数，而是返回此函数。你可以自己决定何时调用以及是否调用。 dependencies：有关是否更新 fn 的所有响应式值的一个列
- [ ] react_reference_react_useImperativeHandle.md-2  —  对应的之前值。如果一次重新渲染导致某些依赖项发生了改变，或你没有提供这个参数列表，你的函数 createHandle 将会被重新执行，而新生成的句柄则会被分配给 ref。 ### 注意 从 React
- [ ] react_reference_react_useMemo.md-2  —  pendencies：所有在 calculateValue 函数中使用的响应式变量组成的数组。响应式变量包括 props、state 和所有你直接在组件中定义的变量和函数。如果你在代码检查工具中 配置
- [ ] react_reference_react_useMemo.md-3  —  帮你发现意外的错误，React 将会 调用你的计算函数两次。这只是一个开发环境下的行为，并不会影响到生产环境。如果计算函数是一个纯函数（它本来就应该是），这将不会影响到代码逻辑。其中一次的调用结果将被
- [ ] react_reference_rules_components-and-hooks-must-be-pure.md-7  —  在渲染中 执行，因为 React 可能会多次渲染组件以提供最佳的用户体验。 ### 注意 副作用是一个比 Effect 更广泛的概念。Effect 特指被包裹在 useEffect 中的代码，而“副作

### 76. [语义改写] useEffect 里返回的清理函数，在组件被移除时会执行吗？

- [x] react_learn_synchronizing-with-effects.md-25  —  。 ``` useEffect(() => { const connection = createConnection(); connection.connect(); return () => { 
- [ ] react_learn_synchronizing-with-effects.md-3  —  通过指定 依赖项 来学习如何控制这一点。 - 必要时添加清理操作。一些 Effect 需要指定如何停止、撤销，或者清除它们所执行的操作。例如，“连接”需要“断开”，“订阅”需要“退订”，而“获取数据”
- [ ] react_learn_synchronizing-with-effects.md-41  —  次，以验证你是否正确实现了清理操作。 现在编辑输入框，输入 abc。如果输入速度足够快，你会看到 调度 "ab" 日志，紧接着 取消 "ab" 日志 和 调度 "abc" 日志。React 总是在执行
- [ ] react_learn_synchronizing-with-effects.md-47  —  'travel' 聊天室。 #### 组件卸载 最后，假设用户离开了当前页面，ChatRoom 组件被卸载。React 执行上一个运行的 Effect 的清理函数，也就是第三次渲染时的 Effect。
- [ ] react_reference_react_Activity.md-31  —  都会被清理。从概念上讲，这些子组件已被卸载，但 React 会保存它们的状态以便后续使用。这是 Activity 的一项特性，因为它意味着隐藏的 UI 部分不会维持活跃的订阅，从而减少了处理隐藏内容所
- [ ] react_reference_react_useEffect.md-6  —  Effect(() => { const connection = createConnection(serverUrl, roomId); connection.connect(); return 
- [ ] react_reference_react_useLayoutEffect.md-3  —  压力测试，确保 cleanup 逻辑“映照”到 setup 逻辑，并停止或撤消 setup 函数正在做的任何事情。如果这导致一个问题，请实现清理函数。 如果你的一些依赖项是组件内部定义的对象或函数，则
- [ ] vue_router_zh_api_interfaces_Router.md-3  —  defined> | 要加入的导航守卫 | #### 返回值 fn ▸ (): void 添加一个导航守卫，它会在每次导航之前被执行。返回一个用来移除该钩子的函数。 返回值 void ### befo

### 77. [概念术语] 在 Vue 中，ref 这个特殊属性是用来做什么的？

- [x] vue_api_built-in-special-attributes.md-1  —  触发。 * 参考指南 - 列表渲染 - 通过 key 管理状态 ## ref 用于注册模板引用。 * 预期：string | Function * 详细信息 ref 用于注册元素或子组件的引用。 使用
- [ ] react_reference_react_createElement.md-7  —  元素究竟是什么？ 显示更多 元素是用来描述一部分用户界面的轻量级结构。比如，<Greeting name="泰勒" /> 和 createElement(Greeting, { name: '泰勒' 
- [ ] vue_api_reactivity-core.md-8  —  void stop: () => void } * 详细信息 第一个参数就是要运行的副作用函数。这个副作用函数的参数也是一个函数，用来注册清理回调。清理回调会在该副作用下一次执行前被调用，可以用来清理
- [ ] vue_guide_essentials_reactivity-fundamentals.md-5  —  }} 在演练场中尝试一下 中的顶层的导入、声明的变量和函数可在同一组件的模板中直接使用。你可以理解为模板是在同一作用域内声明的一个 JavaScript 函数——它自然可以访问与它一起声明的所有内容。
- [ ] vue_guide_essentials_reactivity-fundamentals.md-6  —  踪它的组件的一次重新渲染。 在标准的 JavaScript 中，检测普通变量的访问或修改是行不通的。然而，我们可以通过 getter 和 setter 方法来拦截对象属性的 get 和 set 操作。
- [ ] vue_guide_extras_composition-api-faq.md-0  —  # 组合式 API 常见问答 这个 FAQ 假定你已经有一些使用 Vue 的经验，特别是用选项式 API 使用 Vue 2 的经验。 ## 什么是组合式 API？ 组合式 API (Compositi
- [ ] vue_guide_extras_composition-api-faq.md-7  —  组合式 API 是否覆盖了所有场景？ 组合式 API 能够覆盖所有状态逻辑方面的需求。除此之外，只需要用到一小部分选项：props，emits，name 和 inheritAttrs。 从 3.3 开
- [ ] vue_guide_extras_reactivity-in-dep.md-9  —  组合式 API。 ## 运行时 vs. 编译时响应性 Vue 的响应式系统基本是基于运行时的。追踪和触发都是在浏览器中运行时进行的。运行时响应性的优点是，它可以在没有构建步骤的情况下工作，而且边界情况
- [ ] vue_guide_extras_reactivity-in-dep.md-14  —  (例如，当一个外部的解决方案也用了 Proxy 时)。 将 Vue 的响应性系统与外部状态管理方案集成的大致思路是：将外部状态放在一个 shallowRef 中。一个浅层的 ref 中只有它的 .va
- [ ] vue_guide_extras_reactivity-in-depth.md-14  —  (例如，当一个外部的解决方案也用了 Proxy 时)。 将 Vue 的响应性系统与外部状态管理方案集成的大致思路是：将外部状态放在一个 shallowRef 中。一个浅层的 ref 中只有它的 .va
- [ ] vue_guide_extras_web-components.md-5  —  k 初次调用时，一个 Vue 自定义元素会在内部挂载一个 Vue 组件实例到它的 shadow root 上。 * 当此元素的 disconnectedCallback 被调用时，Vue 会在一个微任

### 78. [命名精确] 使用选项式 API 时，通过 ref 注册的模板引用会被存放在组件的哪个对象上？

- [x] vue_api_built-in-special-attributes.md-1  —  触发。 * 参考指南 - 列表渲染 - 通过 key 管理状态 ## ref 用于注册模板引用。 * 预期：string | Function * 详细信息 ref 用于注册元素或子组件的引用。 使用
- [ ] react_reference_react_useRef.md-2  —  用两次组件方法，这是为了 帮助发现意外问题。但这只是开发模式下的行为，不会影响生产模式。每个 ref 对象都将会创建两次，但是其中一个版本将被丢弃。如果使用的是组件纯函数（也应当如此），那么这不会影响
- [ ] vue_api_composition-api-setup.md-0  —  # 组合式 API：setup() ## 基本使用 setup() 钩子是在组件中使用组合式 API 的入口，通常只在以下情况下使用： 1. 需要在非单文件组件中使用组合式 API 时。 2. 需要在
- [ ] vue_guide_essentials_reactivity-fundamentals.md-5  —  }} 在演练场中尝试一下 中的顶层的导入、声明的变量和函数可在同一组件的模板中直接使用。你可以理解为模板是在同一作用域内声明的一个 JavaScript 函数——它自然可以访问与它一起声明的所有内容。
- [ ] vue_guide_essentials_template-refs.md-2  —  都会被暴露在 this.$refs 之上： vue export default { mounted() { this.$refs.input.focus() } } 注意，你只可以在组件挂载后才能访
- [ ] vue_guide_extras_composition-api-faq.md-7  —  组合式 API 是否覆盖了所有场景？ 组合式 API 能够覆盖所有状态逻辑方面的需求。除此之外，只需要用到一小部分选项：props，emits，name 和 inheritAttrs。 从 3.3 开
- [ ] vue_guide_extras_render-function.md-19  —  n, 200, 'top', { animate: true }] ]) 当一个指令是以名称注册并且不能被直接导入时，可以使用 resolveDirective 函数来解决这个问题。 ### 模板引用
- [ ] vue_guide_extras_render-function.md-20  —  { setup() { const divEl = ref() // return () => h('div', { ref: divEl }) } } 在选项式 API 中，模板引用通过在 vnod
- [ ] vue_guide_typescript_composition-api.md-14  —  引用标注类型 在 Vue 3.5 和 @vue/language-tools 2.1 (为 IDE 语言服务和 vue-tsc 提供支持) 中，在单文件组件中由 useTemplateRef() 创建

### 79. [概念术语] 在 Vue 中，如何为 TransitionGroup 里移动的元素设置自定义的过渡 class？

- [x] vue_guide_built-ins_transition-group.md-2  —  absolute; } 现在它看起来好多了，甚至对整个列表执行洗牌的动画也都非常流畅： 完整的示例 ### 自定义过渡组 class 你还可以通过向 传递 moveClass prop 为移动元素指定
- [ ] vue_api_built-in-components.md-0  —  # 内置组件 内置组件无需注册便可以直接在模板中使用。它们也支持 tree-shake：仅在使用时才会包含在构建中。 在渲染函数中使用它们时，需要显式导入。例如： js import { h, Tra
- [ ] vue_api_built-in-components.md-3  —  南 - ## 为列表中的多个元素或组件提供过渡效果。 * Props 拥有与 除了 mode 以外所有的 props，并增加了两个额外的 props： ts interface TransitionG
- [ ] vue_guide_built-ins_transition-group.md-0  —  # TransitionGroup 是一个内置组件，用于对 v-for 列表中的元素或组件的插入、移除和顺序改变添加动画效果。 ## 和 的区别 支持和 基本相同的 props、CSS 过渡 clas
- [ ] vue_guide_built-ins_transition.md-1  —  nter-active, .v-leave-active { transition: opacity 0.5s ease; } .v-enter-from, .v-leave-to { opacity
- [ ] vue_guide_built-ins_transition.md-3  —  leave-from 被移除的同时)，在过渡或动画完成之后移除。 v-enter-active 和 v-leave-active 给我们提供了为进入和离开动画指定不同速度曲线的能力，我们将在下面的小节
- [ ] vue_guide_built-ins_transition.md-6  —  0% { transform: scale(1); } } 在演练场中尝试一下 在演练场中尝试一下 ### 自定义过渡 class 你也可以向 传递以下的 props 来指定自定义的过渡 class：

### 80. [命名精确] 实现渐进延迟列表动画时，需要把元素的索引渲染到哪个 data attribute 上？

- [x] vue_guide_built-ins_transition-group.md-2  —  absolute; } 现在它看起来好多了，甚至对整个列表执行洗牌的动画也都非常流畅： 完整的示例 ### 自定义过渡组 class 你还可以通过向 传递 moveClass prop 为移动元素指定
- [ ] react_reference_react_useDeferredValue.md-8  —  target.value)} /> </label> <Suspense fallback={<h2>Loading...</h2>}> <SearchResults query={deferredQ
- [ ] vue_api_built-in-components.md-4  —  e attribute 推导，或使用 move-class prop 显式配置)。如果使其位移的 class 被添加时 CSS 的 transform 属性是“可过渡的”，那么该元素会基于 FLIP 
- [ ] vue_guide_built-ins_transition-group.md-0  —  # TransitionGroup 是一个内置组件，用于对 v-for 列表中的元素或组件的插入、移除和顺序改变添加动画效果。 ## 和 的区别 支持和 基本相同的 props、CSS 过渡 clas
- [ ] vue_guide_built-ins_transition-group.md-3  —  g }} 接着，在 JavaScript 钩子中，我们基于当前元素的 data attribute 对该元素的进场动画添加一个延迟。以下是一个基于 GSAP 库的动画示例： js{5} functio
- [ ] vue_guide_built-ins_transition.md-9  —  过渡中，期望的行为应该是等待所有内部元素的过渡完成。 在这种情况下，你可以通过向 组件传入 duration prop 来显式指定过渡的持续时间 (以毫秒为单位)。总持续时间应该匹配延迟加上内部元素的
- [ ] vue_guide_essentials_lis.md-5  —  * 避免渲染应该隐藏的列表 (例如 v-for="user in users" v-if="shouldShowUsers")。在这种情况下，将 v-if 移至容器元素 (如 ul、ol)。 ## 通
- [ ] vue_guide_essentials_list.md-5  —  * 避免渲染应该隐藏的列表 (例如 v-for="user in users" v-if="shouldShowUsers")。在这种情况下，将 v-if 移至容器元素 (如 ul、ol)。 ## 通
