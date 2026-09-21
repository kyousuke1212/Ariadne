API 参考组件 Copy pageCopy
# <Suspense>
<Suspense> 允许在子组件完成加载前展示后备方案。
```
<Suspense fallback={<Loading />}>  <SomeComponent /></Suspense>
```
参考
- <Suspense>
用法
- 当内容正在加载时显示后备方案
- 同时展示内容
- 逐步加载内容
- 在新内容加载时展示过时内容
- 阻止隐藏已经显示的内容
- 表明 Transition 正在发生
- 在导航时重置 Suspense 边界
- 为服务器错误和客户端内容提供后备方案
故障排除
- 如何阻止 UI 在更新期间被后备方案替换
## 参考
### <Suspense>
#### 参数
- children：真正的 UI 渲染内容。如果 children 在渲染中被挂起，Suspense 边界将会渲染 fallback。
- fallback：真正的 UI 未渲染完成时代替其渲染的备用 UI，它可以是任何有效的 React 节点。后备方案通常是一个轻量的占位符，例如表示加载中的图标或者骨架屏。当 children 被挂起时，Suspense 将自动切换至渲染 fallback；当数据准备好时，又会自动切换至渲染 children。如果 fallback 在渲染中被挂起，那么将自动激活最近的 Suspense 边界。
#### 注意
- 在组件首次挂载前，如果组件被挂起，那么 React 将不会保留其任何状态。当组件完成加载后，React 将从头开始重新尝试渲染被挂起的组件树。
- 如果 Suspense 正在展示 React 组件树中的内容，那么当再次被挂起时，除非导致此处更新是由 startTransition 或 useDeferredValue 引起，否则 Suspense 将展示 fallback。
- 如果 React 需要隐藏被再次挂起的可见内容，它将清理内容树中的 layout Effect。当内容可以被再次展示时，React 将重新触发 layout Effect。这确保了测量 DOM 布局的 Effect 不会在内容不可见时运行。
- React 带有内置优化，例如 流式服务器渲染（Streaming Server Rendering） 和 Selective Hydration，它们已经与 Suspense 集成。参见 架构概述 并观看 技术讲座 以了解更多。
## 用法
### 当内容正在加载时显示后备方案
你可以使用 Suspense 边界包裹你应用的任何部分：
```
<Suspense fallback={<Loading />}>  <Albums /></Suspense>
```
React 将展示 后备方案 直到  children  需要的所有代码和数据都加载完成。
在下面的例子中，Albums 组件在获取专辑列表时被 挂起。在它准备好渲染前，Albums 祖先组件中距离其最近的 Suspense 将展示后备方案 —— 即 Loading 组件。当数据加载完成时，React 会隐藏 Loading 后备方案并渲染带有数据的 Albums 组件。
```
ArtistPage.jsAlbums.jsArtistPage.jsReloadClearForkimport { Suspense } from 'react';
import Albums from './Albums.js';

export default function ArtistPage({ artist }) {
  return (
    <>
      <h1>{artist.name}</h1>
      <Suspense fallback={<Loading />}>
        <Albums artistId={artist.id} />
      </Suspense>
    </>
  );
}

function Loading() {
  return <h2>🌀 Loading...</h2>;
}
```
显示更多
### 注意
只有启用了 Suspense 的数据源才会激活 Suspense 组件，它们包括：
- 支持 Suspense 的框架如 Relay 和 Next.js。
- 使用 lazy 懒加载组件代码。
- 使用 use 读取缓存的 Promise 值。
Suspense 无法 检测在 Effect 或事件处理程序中获取数据的情况。
在上面的 Albums 组件中，正确的数据加载方法取决于你使用的框架。如果你使用了支持 Suspense 的框架，你会在其数据获取文档中找到详细信息。
目前尚不支持在不使用固定框架的情况下进行启用 Suspense 的数据获取。实现支持 Suspense 数据源的要求是不稳定的，也没有文档。React 将在未来的版本中发布官方 API，用于与 Suspense 集成数据源。
### 同时展示内容
默认情况下，Suspense 内部的整棵组件树都被视为一个单独的单元。例如，即使 只有一个 组件因等待数据而被挂起，Suspense 内部的整棵组件树中的 所有 的组件都将被替换为加载中指示器：
```
<Suspense fallback={<Loading />}>  <Biography />  <Panel>    <Albums />  </Panel></Suspense>
```
然后，当它们都准备好展示时，它们将一起出现。
在下面的例子中，Biography 和 Albums 都会获取一些数据。但是由于它们都处于同一个 Suspense 下，所以这些组件总是一起“浮现”。
```
ArtistPage.jsPanel.jsBiography.jsAlbums.jsArtistPage.jsReloadClearForkimport { Suspense } from 'react';
import Albums from './Albums.js';
import Biography from './Biography.js';
import Panel from './Panel.js';

export default function ArtistPage({ artist }) {
  return (
    <>
      <h1>{artist.name}</h1>
      <Suspense fallback={<Loading />}>
        <Biography artistId={artist.id} />
        <Panel>
          <Albums artistId={artist.id} />
        </Panel>
      </Suspense>
    </>
  );
}

function Loading() {
  return <h2>🌀 Loading...</h2>;
}
```
显示更多
加载数据的组件不必是 Suspense 边界的直接子组件。例如，你可以将 Biography 和 Albums 移动到一个新的 Details 组件中——这不会改变其行为。Biography 和 Albums 共享最近的父级 <Suspense> 边界，因此它们是同时显示的。
```
<Suspense fallback={<Loading />}>  <Details artistId={artist.id} /></Suspense>function Details({ artistId }) {  return (    <>      <Biography artistId={artistId} />      <Panel>        <Albums artistId={artistId} />      </Panel>    </>  );}
```
### 逐步加载内容
当一个组件被挂起时，最近的父级 Suspense 组件会展示后备方案。这允许你嵌套多个 Suspense 组件创建一个加载序列。每个 Suspense 边界的后备方案都会在下一级内容可用时填充。例如，你可以给专辑列表设置自己的后备方案
```
<Suspense fallback={<BigSpinner />}>  <Biography />  <Suspense fallback={<AlbumsGlimmer />}>    <Panel>      <Albums />    </Panel>  </Suspense></Suspense>
```
调整之后，Biography 不需要“等待” Albums 加载完成就可以展示。
加载序列将会是：
- 如果 Biography 没有加载完成，BigSpinner 会显示在整个内容区域的位置。
- 一旦 Biography 加载完成，BigSpinner 会被内容替换。
- 如果 Albums 没有加载完成，AlbumsGlimmer 会显示在 Albums 和它的父级 Panel 的位置。
- 最后，一旦 Albums 加载完成，它会替换 AlbumsGlimmer。
```
ArtistPage.jsPanel.jsBiography.jsAlbums.jsArtistPage.jsReloadClearForkimport { Suspense } from 'react';
import Albums from './Albums.js';
import Biography from './Biography.js';
import Panel from './Panel.js';

export default function ArtistPage({ artist }) {
  return (
    <>
      <h1>{artist.name}</h1>
      <Suspense fallback={<BigSpinner />}>
        <Biography artistId={artist.id} />
        <Suspense fallback={<AlbumsGlimmer />}>
          <Panel>
            <Albums artistId={artist.id} />
          </Panel>
        </Suspense>
      </Suspense>
    </>
  );
}

function BigSpinner() {
  return <h2>🌀 Loading...</h2>;
}

function AlbumsGlimmer() {
  return (
    <div className="glimmer-panel">
      <div className="glimmer-line" />
      <div className="glimmer-line" />
      <div className="glimmer-line" />
    </div>
  );
}
```
显示更多
Suspense 边界允许协调 UI 的哪些部分应该总是一起“浮现”，以及哪些部分应该按照加载状态的序列逐步显示更多内容。你可以在树的任何位置添加、移动或删除 Suspense 边界，而不会影响应用程序的其余的行为。
不要在每个组件周围都放置 Suspense 边界。为了提供更好的用户体验，Suspense 边界的粒度应该与期望的加载粒度相匹配。如果你与设计师合作，请询问他们应该放置加载状态的位置——他们很可能已经在设计线框图中包含了它们。
### 在新内容加载时展示过时内容
在这个例子中，SearchResults 组件在获取搜索结果时被挂起。输入 "a"，等待结果，然后将其编辑为 "ab"。"a" 的结果将被加载中的后备方案替换。
```
App.jsSearchResults.jsApp.jsReloadClearForkimport { Suspense, useState } from 'react';
import SearchResults from './SearchResults.js';

export default function App() {
  const [query, setQuery] = useState('');
  return (
    <>
      <label>
        Search albums:
        <input value={query} onChange={e => setQuery(e.target.value)} />
      </label>
      <Suspense fallback={<h2>Loading...</h2>}>
        <SearchResults query={query} />
      </Suspense>
    </>
  );
}
```
显示更多
一个常见的替代 UI 模式是 延迟 更新列表，并在新的结果准备好之前，总是显示之前的结果。useDeferredValue Hook 允许你传递一个延迟版本的查询：
```
export default function App() {  const [query, setQuery] = useState('');  const deferredQuery = useDeferredValue(query);  return (    <>      <label>        Search albums:        <input value={query} onChange={e => setQuery(e.target.value)} />      </label>      <Suspense fallback={<h2>Loading...</h2>}>        <SearchResults query={deferredQuery} />      </Suspense>    </>  );}
```
query 将立即更新，所以输入框会显示新的值。然而，deferredQuery 将保持它之前的值，直到数据加载完成，所以 SearchResults 会显示过时的结果一会儿。
为了让用户更容易理解，可以在显示过时的结果列表时添加一个视觉指示：
```
<div style={{  opacity: query !== deferredQuery ? 0.5 : 1}}>  <SearchResults query={deferredQuery} /></div>
```
在下面的例子中，输入 "a"，等待结果加载，然后编辑输入为 "ab"。注意，你现在看到的不是 Suspense 的后备方案，而是暗淡的过时结果列表，直到新的结果加载完成：
```
App.jsApp.jsReloadClearForkimport { Suspense, useState, useDeferredValue } from 'react';
import SearchResults from './SearchResults.js';

export default function App() {
  const [query, setQuery] = useState('');
  const deferredQuery = useDeferredValue(query);
  const isStale = query !== deferredQuery;
  return (
    <>
      <label>
        Search albums:
        <input value={query} onChange={e => setQuery(e.target.value)} />
      </label>
      <Suspense fallback={<h2>Loading...</h2>}>
        <div style={{ opacity: isStale ? 0.5 : 1 }}>
          <SearchResults query={deferredQuery} />
        </div>
      </Suspense>
    </>
  );
}
```
显示更多
### 注意
延迟值和 transition 都可以让你避免显示 Suspense 后备方案，而是使用内联指示器。transition 将整个更新标记为非紧急的，因此它们通常由框架和路由库用于导航。另一方面，延迟值在你希望将 UI 的一部分标记为非紧急，并让它“落后于” UI 的其余部分时非常有用。
### 阻止隐藏已经显示的内容
当一个组件被挂起时，最近的 Suspense 边界会切换到显示后备方案。如果它已经显示了一些内容，这可能会导致令人不快的用户体验。试着按下这个按钮：
```
App.jsLayout.jsIndexPage.jsArtistPage.jsAlbums.jsBiography.jsPanel.jsApp.jsReloadClearForkimport { Suspense, useState } from 'react';
import IndexPage from './IndexPage.js';
import ArtistPage from './ArtistPage.js';
import Layout from './Layout.js';

export default function App() {
  return (
    <Suspense fallback={<BigSpinner />}>
      <Router />
    </Suspense>
  );
}

function Router() {
  const [page, setPage] = useState('/');

  function navigate(url) {
    setPage(url);
  }

  let content;
  if (page === '/') {
    content = (
      <IndexPage navigate={navigate} />
    );
  } else if (page === '/the-beatles') {
    content = (
      <ArtistPage
        artist={{
          id: 'the-beatles',
          name: 'The Beatles',
        }}
      />
    );
  }
  return (
    <Layout>
      {content}
    </Layout>
  );
}

function BigSpinner() {
  return <h2>🌀 Loading...</h2>;
}
```
显示更多
当你按下按钮时，Router 组件渲染了 ArtistPage 而不是 IndexPage。因为 ArtistPage 内部的一个组件被挂起，所以最近的 Suspense 边界开始显示后备方案。最近的 Suspense 边界在根附近，所以整个站点布局被 BigSpinner 替换了。
为了阻止这种情况，你可以使用 startTransition 将导航状态更新标记为 transition：
```
function Router() {  const [page, setPage] = useState('/');  function navigate(url) {    startTransition(() => {      setPage(url);    });  }  // ...
```
这告诉 React 这个状态转移是不紧急的，最好继续显示上一页，而不是隐藏任何已经显示的内容。现在点击按钮并等待 Biography 加载：
```
App.jsLayout.jsIndexPage.jsArtistPage.jsAlbums.jsBiography.jsPanel.jsApp.jsReloadClearForkimport { Suspense, startTransition, useState } from 'react';
import IndexPage from './IndexPage.js';
import ArtistPage from './ArtistPage.js';
import Layout from './Layout.js';

export default function App() {
  return (
    <Suspense fallback={<BigSpinner />}>
      <Router />
    </Suspense>
  );
}

function Router() {
  const [page, setPage] = useState('/');

  function navigate(url) {
    startTransition(() => {
      setPage(url);
    });
  }

  let content;
  if (page === '/') {
    content = (
      <IndexPage navigate={navigate} />
    );
  } else if (page === '/the-beatles') {
    content = (
      <ArtistPage
        artist={{
          id: 'the-beatles',
          name: 'The Beatles',
        }}
      />
    );
  }
  return (
    <Layout>
      {content}
    </Layout>
  );
}

function BigSpinner() {
  return <h2>🌀 Loading...</h2>;
}
```
显示更多
transition 并不会等待 所有 内容加载完成。它只会等待足够长的时间，以避免隐藏已经显示的内容。例如，网站 Layout 已经显示，所以将其隐藏在加载中指示器后面是不好的。然而，Albums 周围的嵌套 Suspense 边界是新出现的，所以 Transition 不会等待它。
### 注意
启用了 Suspense 的路由在默认情况下会将导航更新包装至 Transition 中。
### 表明 Transition 正在发生
在上面的例子中，当你点击按钮，没有任何视觉指示表明导航正在进行。为了添加指示器，你可以用 useTransition 替换 startTransition，它会给你一个布尔值 isPending。在下面的例子中，它被用于当 Transition 发生时改变网站头部的样式：
```
App.jsLayout.jsIndexPage.jsArtistPage.jsAlbums.jsBiography.jsPanel.jsApp.jsReloadClearForkimport { Suspense, useState, useTransition } from 'react';
import IndexPage from './IndexPage.js';
import ArtistPage from './ArtistPage.js';
import Layout from './Layout.js';

export default function App() {
  return (
    <Suspense fallback={<BigSpinner />}>
      <Router />
    </Suspense>
  );
}

function Router() {
  const [page, setPage] = useState('/');
  const [isPending, startTransition] = useTransition();

  function navigate(url) {
    startTransition(() => {
      setPage(url);
    });
  }

  let content;
  if (page === '/') {
    content = (
      <IndexPage navigate={navigate} />
    );
  } else if (page === '/the-beatles') {
    content = (
      <ArtistPage
        artist={{
          id: 'the-beatles',
          name: 'The Beatles',
        }}
      />
    );
  }
  return (
    <Layout isPending={isPending}>
      {content}
    </Layout>
  );
}

function BigSpinner() {
  return <h2>🌀 Loading...</h2>;
}
```
显示更多
### 在导航时重置 Suspense 边界
在 Transition 发生时，React 将避免隐藏已经显示的内容。但是，如果你导航到具有不同参数的路由，你可能想告诉 React 它是 不同 的内容。你可以用 key 表示这一点：
```
<ProfilePage key={queryParams.id} />
```
想想在用户的个人资料页面中导航，然后暂停了。如果更新被包装在 Transition 中，它将不会触发已经可见内容的后备方案。这是预期的行为。
然而，现在想象一下你在两个不同的用户资料之间导航。在这种情况下，显示后备方案是有意义的。例如，一个用户的时间线是与另一个用户的时间线是 不同的内容。通过指定一个 key，你可以确保 React 将不同用户的个人资料视为不同的组件，并在导航期间重置 Suspense 边界。集成 Suspense 的路由应该自动执行此操作。
### 为服务器错误和客户端内容提供后备方案
如果你使用过 流式服务器渲染 API（或依赖它们的框架），React 也会使用你的 <Suspense> 边界来处理服务器上的错误。如果组件在服务器上抛出错误，React 将不会中止服务器渲染。相反，它将找到最接近的 <Suspense> 组件并将其后备方案（例如一个加载中指示器）包含到生成的服务端 HTML 中。用户将首先看到一个加载中指示器。
在客户端，React 将尝试再次渲染相同的组件。如果它在客户端也出错，React 将抛出错误并显示最接近的 错误边界。然而，如果它在客户端没有错误，React 将不会向用户显示错误，因为内容最终成功显示了。
你可以使用这个来防止一些组件在服务端渲染。为此，你应该在服务器环境中抛出一个错误，然后将其包装在一个 <Suspense> 边界中，从而使用后备方案替换它们的 HTML：
```
<Suspense fallback={<Loading />}>  <Chat /></Suspense>function Chat() {  if (typeof window === 'undefined') {    throw Error('Chat should only render on the client.');  }  // ……}
```
服务端 HTML 将包含加载中指示器。它将被客户端上的 Chat 组件替换。
## 故障排除
### 如何阻止 UI 在更新期间被后备方案替换
使用后备方案替换一个可见的 UI 会带来令人不快的用户体验。当一个更新导致一个组件被挂起时，而最近的 Suspense 边界已经向用户显示了内容时，这种情况可能发生。
为了防止这种情况发生，使用 startTransition 将更新标记为非紧急的。在 Transition 期间，React 将等待足够的数据加载，以防止不需要的后备方案出现：
```
function handleNextPageClick() {  // 如果此更新被挂起，不会隐藏已经展示的内容  startTransition(() => {    setCurrentPage(currentPage + 1);  });}
```
这将避免隐藏现有内容。然而，任何新渲染的 Suspense 边界仍然会立即显示后备方案，以避免阻塞 UI 并让用户在内容可用时看到内容。
React 只会在非紧急更新期间阻止不必要的后备方案。这意味着它不会阻止紧急更新的 fallback。你必须使用 startTransition 或 useDeferredValue 这样的 API 来选择性的优化。
如果你的路由集成了 Suspense，它将会自动将更新包装到 startTransition 中。