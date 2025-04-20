import axios from 'axios';

export async function generateCommitMessageFromDiff(diff: string): Promise<string> {
    try {
        const response = await axios.post('http://0.0.0.0:8000/generate', { diff });
        return response.data.commit_message;
    } catch (error) {
        console.error('Error generating commit message');
        return '';
    }
}
