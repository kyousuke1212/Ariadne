API 参考配置 Copy pageCopy
# panicThreshold
panicThreshold 选项用于控制 React 编译器在编译过程中如何处理错误。
```
{  panicThreshold: 'none' // 推荐}
```
参考
- panicThreshold
用法
- 生产环境配置（推荐）
- 开发调试
## 参考
### panicThreshold
决定编译错误是导致构建失败，还是仅跳过优化。
#### 类型
```
'none' | 'critical_errors' | 'all_errors'
```
#### 默认值
'none'
#### 选项
- 'none' (默认, 推荐): 跳过无法编译的组件并继续构建
- 'critical_errors': 仅在关键编译器错误时使构建失败
- 'all_errors': 遇到任何编译诊断即使构建失败
#### 注意事项
- 生产环境构建应始终使用 'none'
- 构建失败会阻止你的应用构建
- 使用 'none' 时，编译器会自动检测并跳过有问题的代码
- 更高的阈值仅在开发调试时有用
## 用法
### 生产环境配置（推荐）
对于生产构建，始终使用 'none'。这是默认值：
```
{  panicThreshold: 'none'}
```
这样可以确保：
- 构建不会因编译器问题而失败
- 无法优化的组件仍可正常运行
- 尽可能多的组件会被优化
- 生产部署更加稳定
### 开发调试
可临时使用更严格的阈值来定位问题：
```
const isDevelopment = process.env.NODE_ENV === 'development';{  panicThreshold: isDevelopment ? 'critical_errors' : 'none',  logger: {    logEvent(filename, event) {      if (isDevelopment && event.kind === 'CompileError') {        // ...      }    }  }}
```