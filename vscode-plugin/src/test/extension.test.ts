// import * as assert from 'assert';

// // You can import and use all API from the 'vscode' module
// // as well as import your extension to test it
// import * as vscode from 'vscode';
// // import * as myExtension from '../../extension';

// suite('Extension Test Suite', () => {
// 	vscode.window.showInformationMessage('Start all tests.');

// 	test('Sample test', () => {
// 		assert.strictEqual(-1, [1, 2, 3].indexOf(5));
// 		assert.strictEqual(-1, [1, 2, 3].indexOf(0));
// 	});
// });



import fs from 'fs';
import path from 'path';
import { generateCommitMessageFromDiff } from '../commentGenerator';

async function runTest() {
    const diff = fs.readFileSync(path.join(__dirname, 'example.diff'), 'utf-8');
    const message = await generateCommitMessageFromDiff(diff);
    console.log(message);
}

runTest();
