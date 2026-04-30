import {test, expect} from '@playwright/test'

test('First Task', async({page}) => {
    await page.goto('https://exampractices.com./')
    const TitleText = page.locator('[class="text-5xl font-bold text-gray-900 mb-6"]')
    await expect(TitleText).not.toContainText('Exam');
    await page.locator('section').locator('h1').locator('[class="text-5xl font-bold text-gray-900 mb-6"]')
    await page.getByTitle('Test Creation Made Simple').isVisible

    
})
