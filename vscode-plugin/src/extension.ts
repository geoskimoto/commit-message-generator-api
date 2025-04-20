import * as vscode from 'vscode';
import simpleGit from 'simple-git';
import { generateCommitMessageFromDiff } from './commentGenerator';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('extension.generateCommitMessage', async () => {
        const diff = await getGitDiff();
        if (!diff) {
            vscode.window.showErrorMessage("No staged changes found!");
            return;
        }

        const commitMessage = await generateCommitMessageFromDiff(diff);

        if (commitMessage) {
            // Open Source Control view
            await vscode.commands.executeCommand('workbench.view.scm');

            const gitExtension = vscode.extensions.getExtension('vscode.git')?.exports;
            if (gitExtension) {
                const api = gitExtension.getAPI(1);
                const repo = api.repositories[0];
                if (repo) {
                    repo.inputBox.value = commitMessage;
                } else {
                    vscode.window.showErrorMessage('No Git repository found.');
                }
            } else {
                vscode.window.showErrorMessage('Git extension not found.');
            }
        }
    });

    context.subscriptions.push(disposable);
}

async function getGitDiff(): Promise<string> {
    try {
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders) {
            vscode.window.showErrorMessage('No workspace folder found.');
            return '';
        }

        const gitInstance = simpleGit(workspaceFolders[0].uri.fsPath);
        const diff = await gitInstance.diff(['--staged']);

        if (!diff.trim()) {
            vscode.window.showWarningMessage('No staged changes found.');
            return '';
        }

        return diff;
    } catch (error) {
        vscode.window.showErrorMessage('Error fetching Git diff: ' + error);
        return '';
    }
}
