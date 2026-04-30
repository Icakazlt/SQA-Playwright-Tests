import {test, expect} from '@playwright/test'

test('Third Task', async({page}) => {
    await page.goto('https://exampractices.com./')
    await page.locator('div').locator('a').locator('[class="text-gray-600 hover:text-gray-900"]')
    await page.getByText('Login').click()
    await expect(page).toHaveURL('https://exampractices.com./login');
})
