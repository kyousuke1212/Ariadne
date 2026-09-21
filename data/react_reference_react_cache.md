API 参考API Copy pageCopy
# cache
### React 服务器组件
- cache 仅供与 React 服务器组件 一起使用。
cache 允许缓存数据获取或计算的结果。
```
const cachedFn = cache(fn);
```
参考
- cache(fn)
用法
- 缓存代价昂贵的计算
- 共享数据快照
- 预加载数据
疑难解答
- 尽管传递的是相同参数，我的记忆化函数仍在重新运行
## 参考
### cache(fn)
在任何组件之外调用 cache 以创建带有缓存的函数版本。
```
import {cache} from 'react';import calculateMetrics from 'lib/metrics';const getMetrics = cache(calculateMetrics);function Chart({data}) {  const report = getMetrics(data);  // ...}
```
当首次使用 data 调用 getMetrics 时，getMetrics 将调用 calculateMetrics(data) 并将结果存储在缓存中。如果再次使用相同的 data 调用 getMetrics，它将返回缓存的结果，而不会再次调用 calculateMetrics(data)。
参见下方更多示例。
#### 参数
- fn：要对其结果进行缓存的函数。fn 可以接受任何参数并返回任何值。
#### 返回值
cache 返回一个与 fn 具有相同类型签名的已缓存版本。在此过程中，它不会调用 fn。
在使用给定的参数调用 cachedFn 时，它首先检查缓存中是否存在缓存的结果。如果存在缓存的结果，它将返回该结果。如果没有，它将使用参数调用 fn，将结果存储在缓存中，并返回该结果。只有在缓存未命中时才会调用 fn。
### 注意
基于输入进行返回值缓存的优化称为 记忆化。我们将从 cache 返回的函数称为一个记忆化函数。
#### 注意
- React 将在每次服务器请求时使所有记忆化函数的缓存失效。
- 每次调用 cache 都会创建一个新函数。这意味着多次使用相同的函数调用 cache 将返回不共享相同缓存的不同记忆化函数。
- cachedFn 还会缓存错误。如果对于某些参数 fn 抛出错误，错误将被缓存，当使用相同参数调用 cachedFn 时，相同的错误将被重新抛出。
- cache 仅供在 服务器组件 中使用。
## 用法
### 缓存代价昂贵的计算
使用 cache 跳过重复工作。
```
import {cache} from 'react';import calculateUserMetrics from 'lib/user';const getUserMetrics = cache(calculateUserMetrics);function Profile({user}) {  const metrics = getUserMetrics(user);  // ...}function TeamReport({users}) {  for (let user in users) {    const metrics = getUserMetrics(user);    // ...  }  // ...}
```
如果相同的 user 对象在 Profile 和 TeamReport 中都被渲染，那么这两个组件可以共享工作，并且只为该 user 调用一次 calculateUserMetrics。
假设首先渲染了 Profile。它将调用 getUserMetrics，并检查是否有缓存的结果。由于这是第一次以该 user 调用 getUserMetrics，所以缓存未命中。于是 getUserMetrics 将会使用 user 调用 calculateUserMetrics 并将结果写入缓存。
当 TeamReport 使用相同的 user 对象来渲染 users 列表时，它将调用 getUserMetrics 并从缓存中读取结果。
如果可以通过传递 AbortSignal 来中止 calculateUserMetrics，则可以使用 cacheSignal()，以便在 React 完成渲染后取消昂贵的计算。calculateUserMetrics 可以直接使用 cacheSignal 在内部处理取消。
### 陷阱
调用不同的记忆化函数将从不同的缓存中读取数据
要访问相同的缓存，组件必须调用同一个记忆化函数。
```
// Temperature.jsimport {cache} from 'react';import {calculateWeekReport} from './report';export function Temperature({cityData}) {  // 🚩 错误示例：在组件中调用 `cache` 会为每次渲染创建新的 `getWeekReport`。  const getWeekReport = cache(calculateWeekReport);  const report = getWeekReport(cityData);  // ...}
```
```
// Precipitation.jsimport {cache} from 'react';import {calculateWeekReport} from './report';// 🚩 错误示例：`getWeekReport` 仅供 `Precipitation` 组件访问。const getWeekReport = cache(calculateWeekReport);export function Precipitation({cityData}) {  const report = getWeekReport(cityData);  // ...}
```
在上面的示例中，Precipitation 和 Temperature 都将调用 cache 创建新的记忆化函数，并使用自己的缓存查找。如果两个组件都使用相同的 cityData 进行渲染，它们将重复调用 calculateWeekReport，进行重复的工作。
此外，Temperature 每次组件渲染时都创建一个 新的记忆化函数，这不允许任何缓存共享。
为了最大化缓存命中率并减少工作量，这两个组件应该调用相同的记忆化函数以访问相同的缓存。因此应该在专用模块中定义记忆化函数，以在不同组件之间使用 import-ed 进行共享。
```
// getWeekReport.jsimport {cache} from 'react';import {calculateWeekReport} from './report';export default cache(calculateWeekReport);
```
```
// Temperature.jsimport getWeekReport from './getWeekReport';export default function Temperature({cityData}) {	const report = getWeekReport(cityData);  // ...}
```
```
// Precipitation.jsimport getWeekReport from './getWeekReport';export default function Precipitation({cityData}) {  const report = getWeekReport(cityData);  // ...}
```
在这里，两个组件都调用从 ./getWeekReport.js 导出的 相同的记忆化函数 来读取和写入相同的缓存。
### 共享数据快照
要在组件之间共享数据快照，请使用类似 fetch 的数据获取函数调用 cache。当多个组件进行相同的数据获取时，只会发出一个请求，并且返回的数据会被缓存并在各个组件之间共享。所有组件在服务器渲染期间都引用相同的数据快照。
```
import {cache} from 'react';import {fetchTemperature} from './api.js';const getTemperature = cache(async (city) => {	return await fetchTemperature(city);});async function AnimatedWeatherCard({city}) {	const temperature = await getTemperature(city);	// ...}async function MinimalWeatherCard({city}) {	const temperature = await getTemperature(city);	// ...}
```
如果 AnimatedWeatherCard 和 MinimalWeatherCard 都为相同的 city 进行渲染，它们将从 记忆化函数 接收相同的数据快照。
如果 AnimatedWeatherCard 和 MinimalWeatherCard 向 getTemperature 提供不同的 city 参数，那么将调用两次 fetchTemperature，并且每个调用站点将接收不同的数据。
city 在其中充当缓存键。
### 注意
异步渲染 只在服务器组件中支持。
```
async function AnimatedWeatherCard({city}) {	const temperature = await getTemperature(city);	// ...}
```
To render components that use asynchronous data in Client Components, see use() documentation.
### 预加载数据
通过缓存长时间运行的数据获取，你可以在渲染组件之前开始异步工作。
```
const getUser = cache(async (id) => {  return await db.user.query(id);});async function Profile({id}) {  const user = await getUser(id);  return (    <section>      <img src={user.profilePic} />      <h2>{user.name}</h2>    </section>  );}function Page({id}) {  // ✅ 正确示例：开始获取用户数据。  getUser(id);  // ……一些计算工作  return (    <>      <Profile id={id} />    </>  );}
```
在渲染 Page 时，组件调用 getUser，但请注意它并不使用返回的数据。这个早期的 getUser 调用会启动异步数据库查询，而在 Page 执行其他计算工作并渲染子组件时进行。
在渲染 Profile 时，我们再次调用 getUser。如果初始 getUser 调用已经返回并缓存了用户数据，那么当 Profile 在 请求并等待这些数据 时，它可以简单地从缓存中读取，而无需进行另一个远程过程调用。如果初始 fetchData 还没有完成，那么在这种模式下预加载数据可以减少数据获取的延迟。
深入探讨
#### 缓存异步工作
显示更多
在评估 异步函数 时，你将收到一个 Promise，该 Promise 包含了该工作的状态（pending，fulfilled，failed）和最终的完成结果。
在这个示例中，异步函数 fetchData 返回一个等待 fetch 的 promise。
```
async function fetchData() {  return await fetch(`https://...`);}const getData = cache(fetchData);async function MyComponent() {  getData();  // ……一些计算工作  await getData();  // ……}
```
在第一次调用 getData 时，从 fetchData 返回的 promise 将被缓存。随后的查找将返回相同的 promise。
请注意，第一次调用 getData 不使用 await，而 第二次 调用会使用。await 是 JavaScript 中的一个操作符，它会等待并返回 promise 的已解决结果。第一次调用 getData 仅启动 fetch 以缓存 promise，以供 第二次 查找。
如果在 第二次 调用时，promise 仍处于 pending 状态，那么 await 会等待结果。优化之处在于，在等待 fetch 的同时，React 可以继续进行计算工作，从而减少了第二次调用的等待时间。
如果 promise 已经解决，无论是得到错误还是 fulfilled 的结果，await 都会立即返回该值。在这两种结果中，都存在性能优势。
### 陷阱
```
在组件外部调用记忆化函数将不使用缓存 import {cache} from 'react';const getUser = cache(async (userId) => {  return await db.user.query(userId);});// 🚩 错误示例：在组件外部调用记忆化函数将不进行记忆化。getUser('demo-id');async function DemoProfile() {  // ✅ 正确示例：`getUser` 将进行记忆化。  const user = await getUser('demo-id');  return <Profile user={user} />;}
```
React 只允许在组件内访问记忆化函数的缓存。在组件外部调用 getUser 时，它仍会评估函数，但不会读取或更新缓存。
这是因为缓存访问是通过 上下文（context） 提供的，而上下文只能从组件中访问。
深入探讨
#### 应该何时使用 cache、memo 和 useMemo？
显示更多
所有提到的 API 都提供了记忆化功能，它们的区别在于记忆化什么、谁可以访问缓存以及何时缓存会失效。
#### useMemo
一般来说，useMemo 用于在客户端组件跨渲染时缓存昂贵的计算。例如，可以用它来记忆化组件内部数据的转换。
```
'use client';function WeatherReport({record}) {  const avgTemp = useMemo(() => calculateAvg(record), record);  // ...}function App() {  const record = getRecord();  return (    <>      <WeatherReport record={record} />      <WeatherReport record={record} />    </>  );}
```
在这个示例中，App 渲染了两个具有相同记录的 WeatherReport。尽管这两个组件都执行相同的工作，但它们无法共享工作。useMemo 的缓存仅在组件内部可用。
但是 useMemo 能够确保如果 App 重新渲染并且 record 对象没有更改，每个组件实例都将跳过工作并使用 avgTemp 的记忆化值。useMemo 仅会缓存具有给定依赖项的 avgTemp 的最后一次计算结果。
#### cache
一般来说，cache 应用于服务器组件以记忆化可以跨组件共享的工作。
```
const cachedFetchReport = cache(fetchReport);function WeatherReport({city}) {  const report = cachedFetchReport(city);  // ...}function App() {  const city = "Los Angeles";  return (    <>      <WeatherReport city={city} />      <WeatherReport city={city} />    </>  );}
```
使用 cache 重新编写前面的示例，在这种情况下，WeatherReport 的第二个实例 将能够跳过重复的工作并从与第一个 WeatherReport 相同的缓存中读取。与前面的示例不同的另一个地方是，cache 也推荐用于 记忆化数据获取，而 useMemo 只应用于计算。
目前 cache 应该仅在服务器组件中使用，并且缓存会在服务器请求之间失效。
#### memo
你应该使用 memo 防止组件在其 props 未更改时重新渲染。
```
'use client';function WeatherReport({record}) {  const avgTemp = calculateAvg(record);  // ...}const MemoWeatherReport = memo(WeatherReport);function App() {  const record = getRecord();  return (    <>      <MemoWeatherReport record={record} />      <MemoWeatherReport record={record} />    </>  );}
```
在这个示例中，两个 MemoWeatherReport 组件在首次渲染时都会调用 calculateAvg。然而，如果 App 重新渲染，但没有更改 record，则没有 props 发生更改，MemoWeatherReport 将不会重新渲染。
与 useMemo 相比，memo 根据 props 而不是特定计算来记忆化组件渲染。与 useMemo 类似，记忆化的组件只缓存了具有最后一组 prop 值的最后一次渲染。一旦 props 更改，缓存将失效，组件将重新渲染。
## 疑难解答
### 尽管传递的是相同参数，我的记忆化函数仍在重新运行
请查看之前提到的常见问题：
- 调用不同的记忆化函数将从不同的缓存中读取。
- 在组件外部调用记忆化函数将不使用缓存。
如果以上问题都不适用，那么可能是与 React 检查缓存中是否存在内容的方式有关。
如果参数不是原始数据类型（例如对象、函数、数组），请确保传递的是相同的对象引用。
在调用记忆化函数时，React 将查找输入参数，以查看是否已经缓存了结果。React 将使用浅相等确定是否存在缓存。
```
import {cache} from 'react';const calculateNorm = cache((vector) => {  // ...});function MapMarker(props) {  // 🚩 错误示例：props 是一个对象，每次渲染时都会更改  const length = calculateNorm(props);  // ...}function App() {  return (    <>      <MapMarker x={10} y={10} z={10} />      <MapMarker x={10} y={10} z={10} />    </>  );}
```
在这种情况下，两个 MapMarker 看起来执行相同的工作，并使用相同的值 {x: 10, y: 10, z: 10} 调用 calculateNorm。尽管这些对象包含相同的值，但它们不是相同的对象引用，因为每个组件都创建了自己的 props 对象。
React 将调用 Object.is 来验证是否存在缓存命中。
```
import {cache} from 'react';const calculateNorm = cache((x, y, z) => {  // ...});function MapMarker(props) {  // ✅ 正确示例：传递原始类型给记忆化函数  const length = calculateNorm(props.x, props.y, props.z);  // ...}function App() {  return (    <>      <MapMarker x={10} y={10} z={10} />      <MapMarker x={10} y={10} z={10} />    </>  );}
```
解决这个问题的一种方法是将向量的维度传递给 calculateNorm。这个方法有效，因为维度本身是原始数据类型。
另一种解决方案可能是将向量对象本身作为一个 prop 传递给组件。我们需要将相同的对象传递给两个组件实例。
```
import {cache} from 'react';const calculateNorm = cache((vector) => {  // ...});function MapMarker(props) {  // ✅ 正确示例：传递相同的 `vector` 对象。  const length = calculateNorm(props.vector);  // ...}function App() {  const vector = [10, 10, 10];  return (    <>      <MapMarker vector={vector} />      <MapMarker vector={vector} />    </>  );}
```