import {test, expect} from '@playwright/test'

test('Fourth Task', async ({ page }) => {
  await page.goto('https://exampractices.com./login');

  const LoginForm = page.locator('form');
  const EmailForm = LoginForm.locator('div').filter({ hasText: "Email" });
  const EmailField = EmailForm.getByRole('textbox');
  const PasswordForm = LoginForm.locator('div').filter({ hasText: "Password" });
  const PassField = PasswordForm.getByRole('textbox');

  await EmailField.fill('test@test.com');
  await PassField.fill('welcome123');

  await LoginForm.getByRole('button').click();
});
