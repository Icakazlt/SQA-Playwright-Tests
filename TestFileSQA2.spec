import {test, expect} from '@playwright/test'

test('Second Task', async({page}) => {
    await page.goto('https://exampractices.com./')
    await page.locator('div').locator('a').locator('[class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700"]')
    await page.getByRole('button', {name: "Sign Up"}).isVisible
    
})
