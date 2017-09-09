from selenium import webdriver

c = webdriver.PhantomJS(executable_path="./phantomjs")
c.set_window_size(1000,1000)

c.get("http://xgxt.cqjtu.edu.cn")
uname = c.find_element_by_id("txtUsername")
upwd = c.find_element_by_id("txtPassword")

uname.send_keys("your_number")
upwd.send_keys("your_password")

sub = c.find_element_by_name("btnLogin")
sub.click()

dormi = c.find_element_by_id("t_nav185")
dormi.click()

fuck = c.find_element_by_link_text("班团干部报送归寝信息")
fuck.click()

final = c.find_element_by_link_text("提交")
final.click()

