# Getting Started

*Tutorial length: ~30 minutes*

## Installation

### Requirements

1. A Running Webserver
2. PHP 5.3+
3. MySQL, MariaDB or other compatible database. With a little work the server
can work against Microsoft SQL Server and others.
4. A Google Authenticator compatible multi-factor authentication app or device
(like [Google Authenticator](https://support.google.com/accounts/answer/1066447?hl=en)
or [Authy](https://www.authy.com/)). **SMS and phone call is not supported**.

**Note: Two-Factor Authentication is forced since a malicious user could push dangerous updates.
This adds another layer of security**

Once you have a running webserver, ensure URL rewriting is enabled and configured
for use with the [Yii 1.1 Framework](http://www.yiiframework.com/). You can find
the configuration for [Apache and Nginx here](http://www.yiiframework.com/doc/guide/1.1/en/quickstart.apache-nginx-config).

## Get the Code

```sh
> git clone https://github.com/ProjectLimitless/UnattendedServer.git Limitless.UnattendedServer
```

Once you have the code, move it to wherever you need for your webserver
configuration. Opening the site should give you a page containing
`Unattended Update Server`.

## Create the Database

In the `db` directory you will find the `unattended.sql` file. This
contains a basic database setup. Execute this file against your database server.
It will create a new `unattended` database.

You will see a sample update in the `updates` table and a demo user in the `users`
table.

## Running the installer

!!! Important
    For the rest of the guide I will assume your server is running at
    **http://unattendedserver.local**. Please change this to wherever your
    server is running. This should also be done for the **download_location** for
    the sample update in the database.


1. Ensure that the `users.ga_secret` column in the database is empty before
starting the installer
2. Open [http://unattendedserver.local/install](http://unattendedserver.local/install)
using your browser.
3. Follow the on-screen instructions.
4. Once installed, use the email address `admin@example.com` together with your
newly chosen password to log in.
5. Once logged in you can change your email address and name.

## Conclusion

Now you have the Unattended Server installed, you can either start [publishing
updates](/publishing-updates) or [get started with Unattended](https://docs.projectlimitless.io/unattended).
