<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container">
            <router-link class="navbar-brand" to="/">EDSystem</router-link>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item active">
                        <router-link class="nav-link" to="/">Главная</router-link>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
                           data-bs-toggle="dropdown" aria-expanded="false">
                            Патежи
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <router-link class="dropdown-item" to="/addpayment">Добавить платеж</router-link>
                            <router-link class="dropdown-item" to="/listpayments">Все платежи</router-link>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <router-link class="dropdown-item" to="/customeraccounts">Счета клиентов</router-link>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown2" role="button"
                           data-bs-toggle="dropdown" aria-expanded="false">
                            Расходы
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <router-link class="dropdown-item" to="/addexpenses">Добавить расход</router-link>
                            <router-link class="dropdown-item" to="/listexpenses">Все расходы</router-link>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <router-link class="dropdown-item" to="/customerexpenses">Расходы клиентов</router-link>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown3" role="button"
                           data-bs-toggle="dropdown" aria-expanded="false">
                            Посылки
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <router-link class="dropdown-item" to="/">Добавить посылку</router-link>
                            <router-link class="dropdown-item" to="/">Все посылки</router-link>
                            <li>
                                <hr class="dropdown-divider">
                            </li>
                            <li><a class="dropdown-item" href="#">Счета клиентов</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown4" role="button" data-bs-toggle="dropdown" aria-expanded="false">Пользователи</a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><router-link class="dropdown-item" to="/adduser">Создать</router-link></li>
                            <li><router-link class="dropdown-item" to="/listusers">Пользователи</router-link></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                    </li>
                    <li class="nav-item">
                        <a class="btn btn-outline-danger" href="/accounts/logout/">Выход</a>
                    </li>

                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
    export default {}
</script>

<style>

</style>