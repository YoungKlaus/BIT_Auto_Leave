# BIT自动请假

百丽宫自动请假脚本

<!-- PROJECT SHIELDS -->

[![Forkers repo roster for @YoungKlaus/BIT_Auto_Leave](https://reporoster.com/forks/YoungKlaus/BIT_Auto_Leave)](https://github.com/YoungKlaus/BIT_Auto_Leave/network/members)
[![Stargazers repo roster for @YoungKlaus/BIT_Auto_Leave](https://reporoster.com/stars/YoungKlaus/BIT_Auto_Leave)](https://github.com/YoungKlaus/BIT_Auto_Leave/stargazers)

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a>
    <img src="https://raw.githubusercontent.com/YoungKlaus/Stickers/main/img/Sticker_%20(9).png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">北京理工大学自动请假</h3>
  <p align="center">
    每日定时（23:00左右）销假请假
    <br />
    <a href="https://github.com/quzard/SEU_Auto_Leave"><strong>本项目修改自SEU_Auto_Leave »</strong></a>
    <br />
    <br />
  </p>

</p>


部署此repo后，每日于北京时间（23:00左右）自动销假请假，每次请假1天（明天），请假理由均为“前往国防科技园”，如有定制化理由，请fork后自行修改BIT_leave.py文件下的qj_data变量，审批制和报备制均可使用。

## 使用步骤
1. star 本项目

2. fork 本项目到自己的仓库

3. 去 Actions 那 Enable Workflow

4. 进入自己 fork 的仓库，点击 Settings -> Secrets -> Action -> New repository secret，依次填入以下所有环境变量（如Name为USERNAME，其Secret为1120210123），它们将作为配置项，在应用启动时传入程序。

**所有的可用 Secrets 及说明**

| Secret     | 解释                                                         |
| ---------- | ------------------------------------------------------------ |
| USERNAME   | 一卡通号                                                     |
| PASSWORD   | 一卡通密码                                                   |
| TELEPHONE  | 联系电话（请假最后一栏需要）                                                   |

4. 如果需要修改上报时间，修改 `.github/workflows/auto_leave.yml`

---------------------------------------------------------------------------
**Action偶先的schedule任务失败的补救方法**

修改BIT_Auto_Leave/.github/workflows/目录下的auto_leave.yaml文件，修改cron定时，尽量避免整点、整5分、整10分这类热门时间，因为github Action共用资源，挤在热门时间触发可能会引发脚本运行失败。不会修改的可以直接拷贝本仓库下的yaml文件，改定时为北京时间23:02。
