# BIT_Auto_Leave
北京理工大学自动请假

## 使用步骤
1. star 本项目

2. fork 本项目到自己的仓库

3. 去 Actions 那 Enable Workflow

4. 进入自己 fork 的仓库，点击 Settings -> Secrets -> New repository secret，它们将作为配置项，在应用启动时传入程序。

**所有的可用 Secrets 及说明**

| Secret     | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| USERNAME   | 一卡通号                                                     |
| PASSWORD   | 一卡通密码                                                   |
| TELEPHONE  | 联系电话（请假最后一栏需要）                                                   |

4. 如果需要修改上报时间，修改 `.github/workflows/auto_leave.yml`
