API 参考配置 Copy pageCopy
# target
target 选项用于指定编译器应为哪个 React 版本生成代码。
```
{  target: '19' // 或 '18' 和 '17'}
```
参考
- target
用法
- 以 React 19 为目标（默认）
- 以 React 17 或 18 为目标
故障排除
- 关于缺少编译器运行环境导致的运行环境错误
- 运行环境包不起作用
- 检查编译输出
## 参考
### target
为编译输出配置目标 React 版本的兼容性。
#### 类型
```
'17' | '18' | '19'
```
#### 默认值
'19'
#### 有效值
- '19': 以 React 19 为目标（默认）。无需额外运行时。
- '18': 以 React 18 为目标。需要安装 react-compiler-runtime 包。
- '17': 以 React 17 为目标。需要安装 react-compiler-runtime 包。
#### 注意事项
- 始终使用字符串值，不要用数字（例如使用 '17' 而非 17）
- 不要包含补丁版本号（例如使用 '18' 而非 '18.2.0'）
- React 19 已内置编译器运行时 API
- React 17 与 18 需要安装 react-compiler-runtime@latest
## 用法
### 以 React 19 为目标（默认）
对于 React 19，无需额外配置：
```
{  // 默认目标为 '19'}
```
编译器会使用 React 19 的内置运行时 API：
```
// 编译输出使用 React 19 的原生 APIimport { c as _c } from 'react/compiler-runtime';
```
### 以 React 17 或 18 为目标
对于 React 17 与 React 18 项目，需要两步：
- 安装运行环境包：
```
npm install react-compiler-runtime@latest
```
- 配置 target:
```
// 对于 React 18{  target: '18'}// 对于 React 17{  target: '17'}
```
编译器会在这两个版本上使用 polyfill 运行环境：
```
// 编译后的输出使用 polyfillimport { c as _c } from 'react-compiler-runtime';
```
## 故障排除
### 关于缺少编译器运行环境导致的运行环境错误
如果你看到类似 “Cannot find module ‘react/compiler-runtime’” 的错误：
检查你的 React 版本:
```
npm why react
```
如果使用 React 17 或 18，安装运行环境：
```
npm install react-compiler-runtime@latest
```
确保你的 target 和你的 React 版本一致：
```
{  target: '18' // 必须与你的 React 主要版本一致}
```
### 运行环境包不起作用
请确保运行环境包：
- 安装在你的项目中（而非全局）
- 被列在 package.json 的依赖中
- 使用正确版本（@latest 标签）
- 不在 devDependencies 中（运行环境需要）
### 检查编译输出
要验证使用的是正确的运行环境，注意导入路径的区别（React 19 使用内置的 react/compiler-runtime，React 17/18 使用独立包 react-compiler-runtime）：
```
// 对于 React 19（内置运行环境）import { c } from 'react/compiler-runtime'//                      ^// 对于 React 17/18（polyfill 运行环境）import { c } from 'react-compiler-runtime'//                      ^
```