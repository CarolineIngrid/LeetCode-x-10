function hasPathSum(root, targetSum) {
    if (!root) {
        // Se a árvore está vazia, não há caminho até a soma alvo
        return false;
    }
    if (!root.left && !root.right) {
        return targetSum === root.val;
    }
    // testar outro depois
    return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
}
