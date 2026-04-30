import {test, expect} from '@playwright/test'


test('Sixt Task', async ({ page }) => {
  await page.goto('https://exampractices.com./register');

  const RegForm = page.locator('form');
  const RegEmail = RegForm.locator('div').filter({ hasText: "Email" });
  const RegEmailField = RegEmail.getByRole('textbox');
  const Reg1stName = RegForm.locator('div').locator('div').filter({ hasText: "First Name" });
  const Reg1stNmField = Reg1stName.getByRole('textbox');
  const RegLastName = RegForm.locator('div').locator('div').filter({ hasText: "Last Name" });
  const RegLstNmField = RegLastName.getByRole('textbox');
  const RegPassField = page.locator('input[name="password"]');
  const PassConfirmField = page.locator('input[name="password_confirm"]');
  await RegEmailField.fill('okoko@oko.ok');
  await Reg1stNmField.fill('Babalau');
  await RegLstNmField.fill('Popoko');
  await RegPassField.fill('passz123');
  await PassConfirmField.fill('passz123');
  await RegForm.getByRole('button').click();
  

});
