# SQL 实验

## 安装数据库软件

<!-- 这里提供 sqlite3、MariaDB 和 MySQL 的安装指南。受限于助教的时间和设备，指南不太完整，如有补充欢迎提交PR。

你也可以选择安装 PostgreSQL 等数据库发行版，并在作业中注明使用的SQL方言。 -->

### sqlite3

#### Linux

```shell
# Arch系
sudo pacman -S --needed sqlite3
# Debian系
sudo apt install sqlite3
```

#### MacOS

对于 macOS 用户，在终端中输入 `sqlite3` 即可使用系统预装软件包

#### Windows

在[官网](https://www.sqlite.org/download.html)下载 `sqlite-tools-win` 软件包，然后添加到系统变量

<!-- ### MariaDB

MariaDB 是 MySQL 被 Oracle收购后，由 MySQL 核心开发者 fork 出来的数据库，与 MySQL高度兼容。Linux 发行版的源中，`mysql`通常其实是指向`mariadb`的。因此 Linux 上建议直接安装 MariaDB。

#### 安装

##### ArchLinux

```shell
sudo pacman -S --needed mariadb
sudo mariadb-install-db --user=mysql --basedir=/usr --datadir=/var/lib/mysql
sudo systemctl start mariadb
```

参考：<https://wiki.archlinux.org/title/MariaDB>

##### Debian

```shell
sudo apt install mariadb-server
sudo systemctl start mariadb 
```

##### MacOS

```shell
brew install mariadb
brew services start mariadb #auto-start MariaDB Server
```

#### 安全加固

```shell
sudo mariadb-secure-installation
```

#### 连入

安装完成之后只有 root 账户，虽然无密码，但是 MariaDB 监听的端口（3306）默认只接受本机的连接，而且拒绝本机上 root 以外的用户连接，所以安全风险其实不大，可以考虑直接用 root 账户完成本实验：

```shell
sudo mariadb
```

然后在里面创建一个数据库（比如`wing`）并使用：

```sql
CREATE DATABASE wing;
use wing;
```

### MySQL

#### 安装

Linux 建议安装 MariaDB。

##### MacOS

使用 brew 或在官网下载安装镜像

```bash
brew install mysql
brew services start mysql
```

##### Windows

推荐在 WSL2 下操作

```bash
sudo apt install mysql-server
sudo service mysql start
```

#### 设置密码

#### 连入

```bash
sudo mysql_secure_installation
sudo mysql -uroot -p
``` -->

## 数据集导入 2pts

我们使用 TPC-H 基准测试程序的数据集作为作业的数据来源。本项目中包含了TPC-H的[specification](tpc-h_v3.0.0.pdf)，你可以在里面 (Page 13)找到每张数据表的schema。

具体来说，我们提供了一些 csv 文件位于```data/```目录下，你们需要首先将其导入数据库中。

我们已经提供了创建表的SQL语句，例如在Linux和mac中可以通过以下方式创建表：

```bash
sqlite3 test.db < schema.sql
```

**请严格按照schema.sql中的schema定义创建对应的表，否则自动评测可能失败**

将数据集导入数据库。导入所需的sqlite命令保存成`load.sql`。

我们在评测初始阶段会运行`sqlite3 test.db < load.sql`，请确保你的`load.sql`能够成功导入数据集。

## 单表查询 5*1pts

对于以下需求，设计 SQL 语句输出结果，你只需要提交对应 SQL 语句。若题目前有括号，则括号内标注了所需要的表。

注意以下语句顺序执行，前序操作可能影响后续结果

1. （`ORDERS`）求 `order` 数大于 20 的 `customer` 的 `O_TOTALPRICE`之和（求和，即每个 customer 返回一条记录）。最终结果中包括`O_CUSTKEY`，`O_TOTALPRICE`之和，以及order的数量。
2. （`LINEITEM`）对 `discount` 大于 0.02 的 `tax` 加 10%
3. （`LINEITEM`）对所有 `tax` 小于 0.05 的物品（`L_ORDERKEY`, `L_LINENUMBER`）按照 `L_ORDERKEY` 计算平均 `discount`。最终结果需满足：
   1. 对结果按平均 `discount` 从大到小排序
   2. 展示平均 `discount` 最大的 10 行

   最终结果中包括 `L_ORDERKEY`和平均 `discount`。
4. （`LINEITEM`）求 `discount` 最大的 `item`，最终结果用 `L_ORDERKEY` 和 `L_LINENUMBER` 表示
   1. 禁止使用 `agg` 操作（即需要用基本运算符表示MAX的逻辑）
5. （`PARTSUPP`）对于相同的 `PS_PARTKEY`，求所有供应商的 `PS_AVAILQTY` 之和。最终结果包括`PS_PARTKEY`和对应的 `PS_AVAILQTY` 之和。

## 多表查询 3*1pts

6. 解释如下 SQL 的作用

   ```sql
   SELECT `C_NAME`, `O_ORDERSTATUS`, `N_NATIONKEY` 
   FROM `customer`, `orders`, `nation` 
   WHERE `C_CUSTKEY`=`O_CUSTKEY` AND `C_NATIONKEY`=`N_NATIONKEY` AND `N_NAME`='CHINA'
   ```

7. （`CUSTOMER`, `ORDERS`）求所有 `total_price` 小于 10000 的 `customer` 行。最终结果包括满足条件的 `customer` 的 所有列。

8. 找到订单(order)来自超过100个**不同**客户(customer)的所有供应商(supplier)。最终结果中包括供应商的名称和不同客户的数量，并按照客户的数量从大到小排序。

## 提交与测试

数据集导入部分提交`load.sql`即可

针对每个查询，提交一个 SQL 文件，文件名为`<题号>.sql` 如 `1.sql`、`2.sql`等，文件内容为你的 SQL 语句。第6题为语言描述，保存`6.txt`即可。

请将所有文件保存至repo的根目录下（和`schema.sql`在一个目录下），并push到自己的作业仓库中。Github CI会自动对你提交的commit进行评测。

我们会使用如下方法测试你的query执行结果并与`outputs/`下的正确结果进行比较：

```bash
sqlite3 test.db < 1.sql
```

不允许修改`outputs/`内的文件和`test.py`，我们在作业截止时会验证这些文件没有被修改。

对于作业若有问题，可以在群聊/网络学堂提问。

## 一些可能有用的链接

<https://www.runoob.com/sqlite/sqlite-tutorial.html>

<!-- <https://www.runoob.com/mysql/mysql-tutorial.html> -->
