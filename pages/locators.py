from selenium.webdriver.common.by import By

class HeaderLocators:
    NAVBAR_LOGO = (By.CSS_SELECTOR, "div.navbar-header")
    NAVBAR_SEARCH = (By.CSS_SELECTOR, ".primary-nav > li > a.btn_search")
    NAVBAR_NEWS = (By.CSS_SELECTOR, "li.dropdown.hover_lg > a")
    NAVBAR_TOOLS = (By.CSS_SELECTOR, "li.dropdown.hover_lg2 > a")
    NAVBAR_LOGIN = (By.CSS_SELECTOR, ".navbar-right > li > a.ir_login_superior")
    NAVBAR_PUBLISH = (By.CSS_SELECTOR, ".navbar-right > li > a.publishAPropertyLink")

    SEARCH_CONTRACT = (By.CSS_SELECTOR, "div.campo_busqueda #mobile-mtiponegocio")
    SEARCH_TYPE = (By.CSS_SELECTOR, "div.campo_busqueda div.campo-selector-multiple")
    SEARCH_LOCATION_INPUT = (By.CSS_SELECTOR, "#mobile-location")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "div.campo_busqueda #btn_submit_search_header")
    SEARCH_LINK = (By.CSS_SELECTOR, "div.busqueda_avanzada div.enlace.campo_busqueda")

    NEWS_SUBSECTIONS = (By.CSS_SELECTOR, "ul.mega-menu_noticias h2.block-title")
    NEWS_TREND_LINKS = (By.CSS_SELECTOR, "ul.not_tendencias > li > a")
    NEWS_ARTICLES = (By.CSS_SELECTOR, "#megamenu1 ul.reportajes > li > a")
    NEWS_MORE_BUTTON = (By.CSS_SELECTOR, "ul.mega-menu_noticias a > button")
    
    TOOLS_SUBSECTIONS = (By.CSS_SELECTOR, "ul.mega-menu_herramientas h2.block-title")
    TOOLS_CALULATOR_LINKS = (By.CSS_SELECTOR, ".fondo_grs > li > a")
    TOOLS_PROPERTY_LINKS = (By.CSS_SELECTOR, ".tu_inmueble > li > a")
    TOOLS_GUIDE_LINKS = (By.CSS_SELECTOR, ".guias > li > a")
    TOOLS_GUIDE_ARTICLES = (By.CSS_SELECTOR, "#megamenu2 ul.reportajes > li > a")
    TOOLS_MORE_BUTTON = (By.CSS_SELECTOR, "ul.mega-menu_herramientas a > button")

    LOGIN_FORM = (By.CSS_SELECTOR, "div > form#fm1")

class CalculatorLocators:
    CALCULATOR_TITLE = (By.CSS_SELECTOR, "div.row h1")
    CREDIT_TAB = (By.CSS_SELECTOR, "a.verprestamo")
    FEE_TAB = (By.CSS_SELECTOR, "a.vercuotas")
    
    MONTHLY_INCOME_INPUT = (By.CSS_SELECTOR, '[name="monthlyIncome"]')
    MONTHLY_INCOME_WARNING = (By.CSS_SELECTOR, "div.formulario.credito p.ng-binding")
    CREDIT_HELP_ICON = (By.CSS_SELECTOR, "div.formulario.credito span.m2-icon-question")
    CREDIT_TOOLTIP = (By.CSS_SELECTOR, "div.formulario.credito span.m2-icon-question > div")
    CREDIT_DURATION_DROPDOWN = (By.CSS_SELECTOR, "div.formulario.credito div.form-group:nth-child(2) select")
    CALCULATE_CREDIT_BUTTON = (By.CSS_SELECTOR, "div.formulario.credito button")
    CREDIT_IMAGE = (By.CSS_SELECTOR, "div.formulario.credito + .imagen")
    CREDIT_RESULTS_TEXTS = (By.CSS_SELECTOR, "div.resultados.credito dt")
    
    LOAN_AMOUNT_INPUT = (By.CSS_SELECTOR, '[name="loadAmount"]')
    LOAN_AMOUNT_WARNING = (By.CSS_SELECTOR, "div.formulario.cuotas p.ng-binding")
    LOAN_DURATION_DROPDOWN = (By.CSS_SELECTOR, "div.formulario.cuotas div.form-group:nth-child(2) select")
    CALCULATE_FEE_BUTTON = (By.CSS_SELECTOR, "div.formulario.cuotas button")
    FEE_IMAGE = (By.CSS_SELECTOR, "div.formulario.cuotas + .imagen")
    FEE_RESULTS_TEXTS = (By.CSS_SELECTOR, "div.resultados.cuotas dt")

class PropertiesLocators:
    PROPERTIES_SECTION = (By.CSS_SELECTOR, "#nuevofooter > div.prefooter_opciones")
    PROPERTIES_TITLE = (By.CSS_SELECTOR, "#prefooter_title")
    PROPERTIES_SUBSECTIONS = (By.CSS_SELECTOR, "div.prefooter_opciones h3")
    SUBSECTION_TITLES = (By.CSS_SELECTOR, "div#section%s h3")
    SUBSECTION_LINKS = (By.CSS_SELECTOR, "div#section%s li")